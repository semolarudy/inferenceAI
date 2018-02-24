import InferenceEngine
from InferenceEngine import HuginClass


def main():
    print "Hi, I'm simple AI. I do probabilistic inference\n Test me"

    print "________________________________________________________________________________________________________________"
    print "Bayesian network XYZ,choose the root"
    jt_xjz = InferenceEngine.jt_xyz_built()
    inference = HuginClass(jt_xjz)
    inference.set_consistency_jt("XY")

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR) WITHOUT EVIDENCE"
    var = inference.jt.get_var_cluster("Y")
    pr = inference.get_prob(var)
    print "\n Prob(", var.name, ")=", pr

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1)"
    inference.enter_evidence("Z", True)
    var = inference.jt.get_var_cluster("Y")
    pr = inference.get_prob(var)
    print "\n Prob(", var.name, "| Z=True )=", pr

    print "\n * Now choose other root"
    jt_xjz = InferenceEngine.jt_xyz_built()
    inference = HuginClass(jt_xjz)
    inference.set_consistency_jt("XZ")

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR) WITHOUT EVIDENCE"
    var = inference.jt.get_var_cluster("Y")
    pr = inference.get_prob(var)
    print "\n Prob(", var.name, ")=", pr

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1)"
    inference.enter_evidence("Z", True)
    var = inference.jt.get_var_cluster("Y")
    pr = inference.get_prob(var)
    print "\n Prob(", var.name, "| Z=True )=", pr

    print "________________________________________________________________________________________________________________"
    print "Fire Bayesian network,choose the root"
    jt = InferenceEngine.built_jt_fire()
    inference = HuginClass(jt)
    inference.set_consistency_jt("AFT")

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR) WITHOUT EVIDENCE"
    var1 = inference.jt.get_var_cluster("Fire")
    pr_single1 = inference.get_prob(var1)
    print "\n Prob(", var1.name, ")=", pr_single1
    var2 = inference.jt.get_var_cluster("Alarm")
    pr_single2 = inference.get_prob(var2)
    print "\n Prob(", var2.name, ")=", pr_single2
    var3 = inference.jt.get_var_cluster("Tampering")
    pr_single3 = inference.get_prob(var3)
    print "\n Prob(", var3.name, ")=", pr_single3

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1)"
    inference.enter_evidence("Fire", True)
    var1 = inference.jt.get_var_cluster("Fire")
    pr_single1 = inference.get_prob(var1)
    print "\n Prob(", var1.name, "= True )=", pr_single1
    var2 = inference.jt.get_var_cluster("Alarm")
    pr_single2 = inference.get_prob(var2)
    print "\n Prob(", var2.name, "| Fire=True )=", pr_single2
    var3 = inference.jt.get_var_cluster("Tampering")
    pr_single3 = inference.get_prob(var3)
    print "\n Prob(", var3.name, "| Fire=True )=", pr_single3

    print "\n * Now choose other root"
    jt = InferenceEngine.built_jt_fire()
    inference = HuginClass(jt)
    inference.set_consistency_jt("FS")

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR) WITHOUT EVIDENCE"
    var1 = inference.jt.get_var_cluster("Fire")
    pr_single1 = inference.get_prob(var1)
    print "\n Prob(", var1.name, ")=", pr_single1
    var2 = inference.jt.get_var_cluster("Alarm")
    pr_single2 = inference.get_prob(var2)
    print "\n Prob(", var2.name, ")=", pr_single2
    var3 = inference.jt.get_var_cluster("Tampering")
    pr_single3 = inference.get_prob(var3)
    print "\n Prob(", var3.name, ")=", pr_single3

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1)"
    inference.enter_evidence("Fire", True)
    var1 = inference.jt.get_var_cluster("Fire")
    pr_single1 = inference.get_prob(var1)
    print "\n Prob(", var1.name, "= True )=", pr_single1
    var2 = inference.jt.get_var_cluster("Alarm")
    pr_single2 = inference.get_prob(var2)
    print "\n Prob(", var2.name, "| Fire=True )=", pr_single2
    var3 = inference.jt.get_var_cluster("Tampering")
    pr_single3 = inference.get_prob(var3)
    print "\n Prob(", var3.name, "| Fire=True )=", pr_single3

    print "________________________________________________________________________________________________________________"
    print "\n  Bayesian network C \n random root and more evidence"
    jt_c = InferenceEngine.jt_c_built()
    inference = HuginClass(jt_c)
    print "variable-> evidence >>>>> probability true"

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR) WITHOUT EVIDENCE"
    inference.get_all_prob()

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1)"
    inference.enter_evidence("c3", True)
    inference.get_all_prob()

    print "-----------------------------------------------------"
    print "SHOW THE Pr(VAR | EVIDENCE1, EVIDENCE2)"
    inference.enter_evidence("c5", False)
    inference.get_all_prob()


if __name__ == "__main__":
    main()
