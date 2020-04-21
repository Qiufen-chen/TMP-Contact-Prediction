#PDBParser.DataFormat
#import Utilities.Files.TxtFileDealer as tf
#import Utilities.Files.FileSysDealer as fs
#import PDBParser.ParserBase

import DataFormat as df
import TxtFileDealer as tf
import FileSysDealer as fs

import PDBParser as pbpp

def func():
    pass

class ParserStructure(object):

    def parseStructure(self, list):
        dict = {}
        current_mark = ""
        for line in list:
            for mark, content in line.items():
                if mark not in ["MODEL", "ATOM", "HETATM", "ANISOU", "SIGUIJ", "ENDMDL", "TER"]:
                    if current_mark != mark:
                        dict.update({mark: []})
                        dict[mark].append(content)
                        current_mark = mark
                    else:
                        dict[mark].append(content)
        dict["REMARK"] = self.remark_classification(dict["REMARK"])
        dict["SEQRES"] = self.seqres_classification(dict["SEQRES"])
        dict["SITE"] = self.site_classification(dict["SITE"])
        dict["CHAINS"] = self.chain_classification(list)
        for mark, content in dict.items():
            print(mark)
            print(content)
        return dict

    def site_classification(self, list):
        site_list = []
        current_sitename = ""
        for content in list:
            if content["siteID"] != current_sitename:
                site = self.init_site(content["siteID"], content["numRes"])
                site_list.append(site)
                current_sitename = content["siteID"]
            if content["resName1"] != "":
                site_res = self.init_site_res(content["chainID1"], content["seq1"], content["resName1"], content["iCode1"])
                for site in site_list:
                    if site["siteID"] == current_sitename:
                        site["resName"].append(site_res)
            if content["resName2"] != "":
                site_res = self.init_site_res(content["chainID2"], content["seq2"], content["resName2"], content["iCode2"])
                for site in site_list:
                    if site["siteID"] == current_sitename:
                        site["resName"].append(site_res)
            if content["resName3"] != "":
                site_res = self.init_site_res(content["chainID3"], content["seq3"], content["resName3"], content["iCode3"])
                for site in site_list:
                    if site["siteID"] == current_sitename:
                        site["resName"].append(site_res)
            if content["resName4"] != "":
                site_res = self.init_site_res(content["chainID4"], content["seq4"], content["resName4"], content["iCode4"])
                for site in site_list:
                    if site["siteID"] == current_sitename:
                        site["resName"].append(site_res)
        return site_list

    def init_site(self, siteID, numRes):
        site = {}
        site["siteID"] = siteID
        site["numRes"] = numRes
        site["resName"] = []
        return site

    def init_site_res(self, chainID, seq, resName, icode):
        res = {}
        res["chainID"] = chainID
        res["seq"] = seq
        res["resName"] = resName
        res["iCode"] = icode
        return res

    def seqres_classification(self, list):
        chain_list = []
        current_chainid = ""
        for content in list:
            if content["chainID"] != current_chainid:
                chain = self.init_seqres(content["chainID"], content["numRes"])
                chain_list.append(chain)
                current_chainid = content["chainID"]
            for chain in chain_list:
                if chain["chainID"] == current_chainid:
                    chain["resName"] += content["resName"]
        return chain_list

    def init_seqres(self, chainID, numRes):
        seqres = {}
        seqres["chainID"] = chainID
        seqres["numRes"] = numRes
        seqres["resName"] = []
        return seqres

    def remark_classification(self, list):
        remark_list = []
        current_remarkNum = 0
        for content in list:
            if content["remarkNum"] != current_remarkNum:
                remark = self.init_remark(content["remarkNum"])
                remark_list.append(remark)
                current_remarkNum = content["remarkNum"]
            for remark in remark_list:
                if remark["remarkNum"] == current_remarkNum:
                    remark["empty"].append(content["empty"])
        # print(remark_list)
        return remark_list

    def init_remark(self, remarkNum):
        remark = {}
        remark["remarkNum"] = remarkNum
        remark["empty"] = []
        return remark

    def chain_classification(self, list):
        chains = self.init_chains(list)
        for line in list:
            for mark, content in line.items():
                if mark == "MODEL" or mark == "ENDMDL":
                    for chain in chains:
                        chain["chainStructure"].append(line)
                if mark == "ATOM" or mark == "HETATM" or mark == "ANISOU" or mark == "SIGUIJ":
                    for chain in chains:
                        if content["chainID"] == chain["chainID"]:
                            chain["chainStructure"].append(line)
        chains = self.chain_to_model(chains)
        return chains

    def init_chains(self, linelist):
        idlist = []
        resultlist = []
        for line in linelist:
            for mark, content in line.items():
                if mark == "ATOM" or mark == "HETATM":
                    if content["chainID"] not in idlist:
                        idlist.append(content["chainID"])
        for chainid in idlist:
            dict1 ={}
            dict1["chainID"] = chainid
            dict1["chainStructure"] = []
            resultlist.append(dict1)
        return resultlist

    def chain_to_model(self, chains):
        for chain in chains:
            model_open = 0
            current_model_id = 0
            model_list = []
            for line in chain["chainStructure"]:
                for mark, content in line.items():
                    if mark == "MODEL":
                        model_open = 1
                        current_model_id = content["serial"]
                        model = self.init_model(current_model_id)
                        model_list.append(self.init_model(current_model_id))
                    if mark == "ATOM" or mark == "HETATM" or mark == "ANISOU" or mark == "SIGUIJ":
                        if model_open == 0:
                            current_model_id = 1
                            model_open = 1
                            model = self.init_model(current_model_id)
                            model_list.append(self.init_model(current_model_id))
                        for model in model_list:
                            if model["serial"] == current_model_id:
                                model["modelStructure"].append(line)
            model_list = self.model_to_residue(model_list)
            chain["chainStructure"] = {"models": model_list}
        return chains

    def model_to_residue(self, models):
        for model in models:
            current_res_id = 0
            res_list = []
            for atoms in model["modelStructure"]:
                for mark, content in atoms.items():
                    if content["resSeq"] != current_res_id:
                        res = self.init_res(content["resName"], content["resSeq"])
                        res_list.append(res)
                        current_res_id = content["resSeq"]
                    for res in res_list:
                        if res["resSeq"] == current_res_id:
                            res["resStructure"].append(atoms)
            model["modelStructure"] = res_list
        return models

    def init_model(self, model_id):
        model = {}
        model["serial"] = model_id
        model["modelStructure"] = []
        return model

    def init_res(self, resName, resSeq):
        res = {}
        res["resName"] = resName
        res["resSeq"] = resSeq
        res["resStructure"] = []
        return res

ps = ParserStructure()
pb = pbpp.ParserBase(func)
pdblist = pb.parser("4zzc.pdb", target="ALL")
# chains = ps.atom_classification(pdblist)
remark =ps.parseStructure(pdblist)