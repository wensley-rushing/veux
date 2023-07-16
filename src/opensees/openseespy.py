from .tcl import TclRuntime

# A list of symbol names that are importable
# from this module. All of these are dynamically
# resolved by the function __getattr__ below.
__all__ = [
    "uniaxialMaterial",
    "testUniaxialMaterial",
    "setStrain",
    "getStrain",
    "getStress",
    "getTangent",
    "getDampTangent",
    "wipe",
    "model",
    "node",
    "fix",
    "element",
    "timeSeries",
    "pattern",
    "load",
    "system",
    "numberer",
    "constraints",
    "integrator",
    "algorithm",
    "analysis",
    "analyze",
    "test",
    "section",
    "fiber",
    "patch",
    "layer",
    "geomTransf",
    "beamIntegration",
    "loadConst",
    "eleLoad",
    "reactions",
    "nodeReaction",
    "eigen",
    "modalProperties",
    "responseSpectrumAnalysis",
    "nDMaterial",
    "block2D",
    "block3D",
    "rayleigh",
    "wipeAnalysis",
    "setTime",
    "remove",
    "mass",
    "equalDOF",
    "nodeEigenvector",
    "getTime",
    "setCreep",
    "eleResponse",
    "sp",
    "fixX",
    "fixY",
    "fixZ",
    "reset",
    "initialize",
    "getLoadFactor",
    "build",
    "printModel",
    "printA",
    "printB",
    "printGID",
    "testNorm",
    "testNorms",
    "testIter",
    "recorder",
    "database",
    "save",
    "restore",
    "eleForce",
    "eleDynamicalForce",
    "nodeUnbalance",
    "nodeDisp",
    "setNodeDisp",
    "nodeVel",
    "setNodeVel",
    "nodeAccel",
    "setNodeAccel",
    "nodeResponse",
    "nodeCoord",
    "setNodeCoord",
    "getPatterns",
    "getFixedNodes",
    "getFixedDOFs",
    "getConstrainedNodes",
    "getConstrainedDOFs",
    "getRetainedNodes",
    "getRetainedDOFs",
    "updateElementDomain",
    "getNDM",
    "getNDF",
    "eleNodes",
    "eleType",
    "nodeDOFs",
    "nodeMass",
    "nodePressure",
    "setNodePressure",
    "nodeBounds",
    "start",
    "stop",
    "modalDamping",
    "modalDampingQ",
    "setElementRayleighDampingFactors",
    "region",
    "setPrecision",
    "searchPeerNGA",
    "domainChange",
    "record",
    "metaData",
    "defaultUnits",
    "stripXML",
    "convertBinaryToText",
    "convertTextToBinary",
    "getEleTags",
    "getCrdTransfTags",
    "getNodeTags",
    "getParamTags",
    "getParamValue",
    "sectionForce",
    "sectionDeformation",
    "sectionStiffness",
    "sectionFlexibility",
    "sectionLocation",
    "sectionWeight",
    "sectionTag",
    "sectionDisplacement",
    "cbdiDisplacement",
    "basicDeformation",
    "basicForce",
    "basicStiffness",
    "InitialStateAnalysis",
    "totalCPU",
    "solveCPU",
    "accelCPU",
    "numFact",
    "numIter",
    "systemSize",
    "version",
    "setMaxOpenFiles",
    "limitCurve",
    "imposedMotion",
    "imposedSupportMotion",
    "groundMotion",
    "equalDOF_Mixed",
    "rigidLink",
    "rigidDiaphragm",
    "ShallowFoundationGen",
    "setElementRayleighFactors",
    "mesh",
    "remesh",
    "parameter",
    "addToParameter",
    "updateParameter",
    "setParameter",
    "getPID",
    "getNP",
    "barrier",
    "send",
    "recv",
    "Bcast",
    "frictionModel",
    "computeGradients",
    "sensitivityAlgorithm",
    "sensNodeDisp",
    "sensNodeVel",
    "sensNodeAccel",
    "sensLambda",
    "sensSectionForce",
    "sensNodePressure",
    "getNumElements",
    "getEleClassTags",
    "getEleLoadClassTags",
    "getEleLoadTags",
    "getEleLoadData",
    "getNodeLoadTags",
    "getNodeLoadData",
    "randomVariable",
    "getRVTags",
    "getRVParamTag",
    "getRVValue",
    "getMean",
    "getStdv",
    "getPDF",
    "getCDF",
    "getInverseCDF",
    "correlate",
    "performanceFunction",
    "gradPerformanceFunction",
    "transformUtoX",
    "wipeReliability",
    "updateMaterialStage",
    "sdfResponse",
    "probabilityTransformation",
    "startPoint",
    "randomNumberGenerator",
    "reliabilityConvergenceCheck",
    "searchDirection",
    "meritFunctionCheck",
    "stepSizeRule",
    "rootFinding",
    "functionEvaluator",
    "gradientEvaluator",
    "getNumThreads",
    "setNumThreads",
    "logFile",
    "setStartNodeTag",
    "hystereticBackbone",
    "stiffnessDegradation",
    "strengthDegradation",
    "strengthControl",
    "unloadingRule",
    "partition",
    "pressureConstraint",
    "domainCommitTag",
    "runFOSMAnalysis",
    "findDesignPoint",
    "runFORMAnalysis",
    "getLSFTags",
    "runImportanceSamplingAnalysis",
    "IGA",
    "NDTest",

    "tcl"
]

def _as_str_arg(arg):
    """
    Convert arg to a string that represents
    Tcl semantics.
    """
    if isinstance(arg, list):
        return f"{{{''.join(_as_str_arg(a) for a in arg)}}}"

    elif isinstance(arg, bool):
        return str(int(arg))

    elif isinstance(arg, dict):
        return "{\n" + "\n".join([
          f"{cmd} " + " ".join(_as_str_arg(a) for a in val)
              for cmd, val in kwds
    ]) + "}"
    else:
        return str(arg)

class OpenSeesPy(TclRuntime):
    """
    This class is meant to be instantiated as a global singleton
    that is private to this Python module.

    It encapsulates an instance of TclRuntime which implements an
    OpenSees state.
    """

    def _str_call(self, proc_name: str, *args, **kwds)->str:
        """
        Invoke the TclRuntime's eval method, calling
        a procedure named `proc_name` with arguments
        from args and kwds, after converting Python semantics
        to Tcl semantics (via _as_str_arg).

        For example, key-word arguments contained in the `kwds`
        dict are converted to a sequence of "-key" and "value"
        strings.
        """

        tcl_args = [_as_str_arg(i) for i in args]
        tcl_args += [
          f"-{key} " + _as_str_arg(val)
              for key, val in kwds.items()
        ]
        cmd = f"{proc_name} " + " ".join(tcl_args)
        try:
            ret = self._interp.tk.eval(cmd)
        except Exception as e:
            print(cmd)
            raise e
        return ret if ret != "" else None

    def pattern(self, *args, **kwds):
        self._current_pattern = args[1]
        return self._str_call("pattern", *args, **kwds)

    def load(self, *args, **kwds):
        pattern = self._current_pattern
        return self._str_call("nodalLoad", *args, "-pattern", pattern, **kwds)


# The global singleton
tcl = _openseespy = OpenSeesPy()

def __getattr__(name):
    # For reference:
    #   https://peps.python.org/pep-0562/#id4
    if name in {"pattern", "load"}:
        return getattr(_openseespy, name)
    else:
        return _openseespy._partial(_openseespy._str_call, name)

