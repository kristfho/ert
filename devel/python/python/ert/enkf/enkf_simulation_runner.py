from ert.cwrap import CWrapper, BaseCClass
from ert.enkf import ENKF_LIB, EnkfFs
from ert.enkf.enums import EnkfInitModeEnum
from ert.util import BoolVector


class EnkfSimulationRunner(BaseCClass):

    def __init__(self, enkf_main):
        assert isinstance(enkf_main, BaseCClass)
        super(EnkfSimulationRunner, self).__init__(enkf_main.from_param(enkf_main).value, parent=enkf_main, is_reference=True)
        self.ert = enkf_main
        """:type: ert.enkf.EnKFMain """

    def runSimpleStep(self, active_realization_mask, initialization_mode, iter_nr):
        """ @rtype: bool """
        assert isinstance(active_realization_mask, BoolVector)
        assert isinstance(initialization_mode, EnkfInitModeEnum)
        return EnkfSimulationRunner.cNamespace().run_simple_step(self, active_realization_mask, initialization_mode , iter_nr)

    def createRunPath(self, active_realization_mask, iter_nr):
        """ @rtype: bool """
        assert isinstance(active_realization_mask, BoolVector)
        return EnkfSimulationRunner.cNamespace().create_run_path(self, active_realization_mask, iter_nr)

    def runEnsembleExperiment(self, active_realization_mask=None):
        """ @rtype: bool """
        if active_realization_mask is None:
            count = self.ert.getEnsembleSize()
            active_realization_mask = BoolVector(default_value=True, initial_size=count)

        iter_nr = 0
        return self.runSimpleStep(active_realization_mask, EnkfInitModeEnum.INIT_CONDITIONAL, iter_nr)


    def runWorkflows(self , runtime):
        """:type ert.enkf.enum.HookRuntimeEnum"""
        hook_manager = self.ert.getHookManager()
        hook_manager.runWorkflows( runtime  , self.ert )




cwrapper = CWrapper(ENKF_LIB)
cwrapper.registerType("enkf_simulation_runner", EnkfSimulationRunner)

EnkfSimulationRunner.cNamespace().run_smoother      = cwrapper.prototype("void enkf_main_run_smoother(enkf_simulation_runner, char*, bool)")
EnkfSimulationRunner.cNamespace().create_run_path   = cwrapper.prototype("bool enkf_main_create_run_path(enkf_simulation_runner, bool_vector, int)")
EnkfSimulationRunner.cNamespace().run_simple_step   = cwrapper.prototype("bool enkf_main_run_simple_step(enkf_simulation_runner, bool_vector, enkf_init_mode_enum, int)")
