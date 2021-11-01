# -*- coding: utf-8 -*-

from unifiedglyphinfo import CollectedGlyphInfos, xpos, ypos


def collect_infos(infos_dict):
    return infos_dict.update(ugi.unified_infos)


ugi = CollectedGlyphInfos()

x = ugi('Alpha')
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Alpha', right='Alpha')

x = ugi('Alphatonos')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')
x.addMetrics(left='Omegadasiavaria', right='Alpha')

x = ugi('Beta')
x.addKerning(left='Eta', right='Beta')
x.addMetrics(left='Eta', right='Beta')

x = ugi('Chi')
x.addKerning(left='Chi', right='Kappa')
x.addMetrics(left='=|Kappa', right='Kappa')

x = ugi('Delta')
x.addKerning(left='Alpha', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')

x = ugi('Epsilon')
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Eta', right='Epsilon')
x.addMetrics(left='Eta', right='Epsilon')

x = ugi('Epsilontonos')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='Omegadasiavaria', right='Epsilon')

x = ugi('Eta')
x.addAnchor('bottom', position_x=xpos.outline_center, position_y=ypos.base_line)
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Eta', right='Eta')

x = ugi('Etatonos')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='Omegadasiavaria', right='Eta')

x = ugi('Gamma')
x.addKerning(left='Eta', right='Gamma')
x.addMetrics(left='Eta', right='Gamma')

x = ugi('Iota')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Eta', right='Eta')

x = ugi('Iotadieresis')
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Eta', right='Eta')

x = ugi('Iotatonos')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='Omegadasiavaria', right='Eta')

x = ugi('Kappa')
x.addKerning(left='Eta', right='Kappa')
x.addMetrics(left='Eta', right='Kappa')

x = ugi('Lambda')
x.addKerning(left='Alpha', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')

x = ugi('Mu')
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Eta', right='Eta')

x = ugi('Nu')
x.addKerning(left='Eta', right='Nu')
x.addMetrics(left='Eta', right='Nu')

x = ugi('Omega')
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Omega', right='Omega')
x.addMetrics(left='Omega', right='Omega')

x = ugi('Omegatonos')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='Omegadasiavaria', right='Omega')

x = ugi('Omicron')
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Omicron', right='Omicron')
x.addMetrics(left='Omicron', right='Omicron')

x = ugi('Omicrontonos')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='Omegadasiavaria', right='Omicron')

x = ugi('Phi')
x.addKerning(left='Phi', right='Phi')
x.addMetrics(left='Phi', right='Phi')

x = ugi('Pi')
x.addKerning(left='Eta', right='Eta')

x = ugi('Psi')
x.addKerning(left='Psi', right='Psi')
x.addMetrics(left='Psi', right='Psi')

x = ugi('Rho')
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Eta', right='Rho')
x.addMetrics(left='Eta', right='Rho')

x = ugi('Sigma')
x.addKerning(left='Sigma', right='Epsilon')
x.addMetrics(left='Sigma', right='Epsilon')

x = ugi('Tau')
x.addKerning(left='Tau', right='Gamma')
x.addMetrics(left='Tau', right='Gamma')

x = ugi('Theta')
x.addKerning(left='Omicron', right='Omicron')
x.addMetrics(left='Omicron', right='Omicron')

x = ugi('Upsilon')
x.addAnchor('top', position_x=xpos.outline_center, position_y=ypos.capHeight)
x.addAnchor('topleft', position_x=xpos.outline_left, position_y=ypos.capHeight)
x.addKerning(left='Upsilon', right='Upsilon')
x.addMetrics(left='Upsilon', right='Upsilon')

x = ugi('Upsilondieresis')
x.addKerning(left='Upsilon', right='Upsilon')
x.addMetrics(left='Upsilon', right='Upsilon')

x = ugi('Upsilontonos')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='Omegadasiavaria', right='Upsilon')

x = ugi('Xi')
x.addKerning(left='Xi', right='Epsilon')
x.addMetrics(left='Xi', right='Epsilon')

x = ugi('Zeta')
x.addKerning(left='Zeta', right='Zeta')
x.addMetrics(left='Zeta', right='Zeta')


#
# --------------------------------
#
#   Lowercase
#
# --------------------------------
#

x = ugi('alpha')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='omicron', right='alpha')

x = ugi('alphatonos')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='omicron', right='alpha')

x = ugi('beta')
x.addKerning(left='beta', right='beta')
x.addMetrics(left='beta', right='beta')

x = ugi('chi')
x.addKerning(left='chi', right='chi')
x.addMetrics(left='chi', right='chi')

x = ugi('delta')
x.addKerning(left='omicron', right='delta')
x.addMetrics(left='omicron', right='delta')

x = ugi('epsilon')
x.addAnchor('top', position_x=xpos.apex_top, position_y=ypos.xHeight)
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilontonos')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('eta')
x.addRecipe('n decompose')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etatonos')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('gamma')
x.addKerning(left='gamma', right='gamma')
x.addMetrics(left='gamma', right='gamma')

x = ugi('iota')
x.addAnchor('top', position_x=xpos.stem_top_center, position_y=ypos.xHeight)
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iota', right='iota')

x = ugi('iotadieresis')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotadieresistonos')
x.addKerning(left='iotadieresistonos', right='iotadieresistonos')
x.addMetrics(left='iotadieresistonos', right='iotadieresistonos')

x = ugi('iotatonos')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotatonos', right='iota')

x = ugi('kappa')
x.addKerning(left='eta', right='kappa')
x.addMetrics(left='eta', right='kappa')

x = ugi('lambda')
x.addKerning(left='lambda', right='lambda')
x.addMetrics(left='lambda', right='lambda')

x = ugi('mu')
x.addKerning(left='mu', right='mu')
x.addMetrics(left='mu', right='mu')

x = ugi('nu')
x.addKerning(left='gamma', right='gamma')
x.addMetrics(left='gamma', right='gamma')

x = ugi('omega')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegatonos')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicron')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicrontonos')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('phi')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('pi')
x.addKerning(left='pi', right='pi')
x.addMetrics(left='pi', right='pi')

x = ugi('psi')
x.addKerning(left='upsilon', right='upsilon')
x.addMetrics(left='upsilon', right='upsilon')

x = ugi('rho')
x.addKerning(left='rho', right='omicron')
x.addMetrics(left='rho', right='omicron')

x = ugi('sigma')
x.addKerning(left='omicron', right='sigma')
x.addMetrics(left='omicron', right='sigma')

x = ugi('sigmafinal')
x.addKerning(left='omicron', right='sigmafinal')
x.addMetrics(left='omicron', right='sigmafinal')

x = ugi('tau')
x.addKerning(left='tau', right='tau')
x.addMetrics(left='tau', right='tau')

x = ugi('theta')
x.addKerning(left='theta', right='theta')
x.addMetrics(left='theta', right='theta')

x = ugi('upsilon')
x.addKerning(left='upsilon', right='upsilon')
x.addMetrics(left='upsilon', right='upsilon')

x = ugi('upsilondieresis')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondieresistonos')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilontonos')
x.addKerning(left='upsilon', right='upsilondieresistonos')
x.addMetrics(left='upsilon', right='upsilondieresistonos')

x = ugi('xi')
x.addKerning(left='xi', right='xi')
x.addMetrics(left='xi', right='xi')

x = ugi('zeta')
x.addKerning(left='zeta', right='zeta')
x.addMetrics(left='zeta', right='zeta')


#
# --------------------------------
#
#   Smallcaps
#
# --------------------------------
#

x = ugi('alpha.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')

x = ugi('alphatonos.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')
x.addKerning(left='omegadasiavaria.sc', right='alpha.sc')

x = ugi('beta.sc')
x.addKerning(left='eta.sc', right='beta.sc')

x = ugi('chi.sc')
x.addKerning(left='chi.sc', right='kappa.sc')

x = ugi('delta.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')

x = ugi('epsilon.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')

x = ugi('epsilontonos.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')
x.addKerning(left='omegadasiavaria.sc', right='epsilon.sc')

x = ugi('eta.sc')
x.addKerning(left='eta.sc', right='eta.sc')

x = ugi('etatonos.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')
x.addKerning(left='omegadasiavaria.sc', right='eta.sc')

x = ugi('gamma.sc')
x.addKerning(left='eta.sc', right='gamma.sc')

x = ugi('iota.sc')
x.addKerning(left='eta.sc', right='eta.sc')

x = ugi('iotadieresis.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')
x.addKerning(left='eta.sc', right='eta.sc')

x = ugi('iotatonos.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')
x.addKerning(left='omegadasiavaria.sc', right='eta.sc')

x = ugi('kappa.sc')
x.addKerning(left='eta.sc', right='kappa.sc')

x = ugi('lambda.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')

x = ugi('mu.sc')
x.addKerning(left='eta.sc', right='eta.sc')

x = ugi('nu.sc')
x.addKerning(left='eta.sc', right='nu.sc')

x = ugi('omega.sc')
x.addKerning(left='omega.sc', right='omega.sc')

x = ugi('omegatonos.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')
x.addKerning(left='omegadasiavaria.sc', right='omega.sc')

x = ugi('omicron.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')

x = ugi('omicrontonos.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')
x.addKerning(left='omegadasiavaria.sc', right='omicron.sc')

x = ugi('phi.sc')
x.addKerning(left='phi.sc', right='phi.sc')

x = ugi('pi.sc')
x.addKerning(left='eta.sc', right='eta.sc')

x = ugi('psi.sc')
x.addKerning(left='psi.sc', right='psi.sc')

x = ugi('rho.sc')
x.addKerning(left='eta.sc', right='rho.sc')

x = ugi('sigma.sc')
x.addKerning(left='sigma.sc', right='epsilon.sc')

x = ugi('tau.sc')
x.addKerning(left='tau.sc', right='gamma.sc')

x = ugi('theta.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')

x = ugi('upsilon.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilondieresis.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilontonos.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')
x.addKerning(left='omegadasiavaria.sc', right='upsilon.sc')

x = ugi('xi.sc')
x.addKerning(left='xi.sc', right='epsilon.sc')

x = ugi('zeta.sc')
x.addKerning(left='zeta.sc', right='zeta.sc')

#
# --------------------------------
#
#   Other
#
# --------------------------------
#

x = ugi('dasia')
x.addRecipe('psili flip_horizontal')

x = ugi('lowernumeral-greek')
x.addRecipe('numeral-greek flip_horizontal flip_vertical')

x = ugi('anoteleia')
x.addMetrics(left='periodcentered', right='periodcentered')


#
# --------------------------------
#
#   Polytonic
#
# --------------------------------
#

x = ugi('Alphadasia')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaoxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaoxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphadasiaoxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphadasiaperispomeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphadasiaperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphadasiavaria')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiavariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiavariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphadasiavariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphadasiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphadasiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphadasiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphamacron')
x.addKerning(left='Alpha', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')

x = ugi('Alphaoxia')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsili')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsilioxia')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsilioxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsilioxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphapsilioxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphapsiliperispomeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsiliperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsiliperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphapsiliperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphapsilivaria')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsilivariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsilivariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphapsilivariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphapsiliypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphapsiliypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphapsiliypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Alphavaria')
x.addKerning(left='Omegadasiavaria', right='Alpha')
x.addMetrics(left='=0', right='Alpha')

x = ugi('Alphavrachy')
x.addKerning(left='Alpha', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')

x = ugi('Alphaypogegrammeni')
x.addKerning(left='Alpha', right='Alpha')
x.addMetrics(left='Alpha', right='Alpha')

x = ugi('Alphaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Alphaypogegrammeni.ss03')
x.addMetrics(left='Alpha', right='iota')

x = ugi('Epsilondasia')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilondasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilondasiavaria')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilonoxia')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilonpsili')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilonpsilioxia')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilonpsilivaria')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Epsilonvaria')
x.addKerning(left='Omegadasiavaria', right='Epsilon')
x.addMetrics(left='=0', right='Epsilon')

x = ugi('Etadasia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaoxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaoxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etadasiaoxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etadasiaperispomeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etadasiaperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etadasiavaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiavariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiavariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etadasiavariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etadasiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etadasiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etadasiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etaoxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsili')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsilioxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsilioxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsilioxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etapsilioxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etapsiliperispomeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsiliperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsiliperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etapsiliperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etapsilivaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsilivariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsilivariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etapsilivariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etapsiliypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etapsiliypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etapsiliypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Etavaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Eta')

x = ugi('Etaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='Eta', right='Eta')

x = ugi('Etaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Etaypogegrammeni.ss03')
x.addMetrics(left='Eta', right='iota')

x = ugi('Iotadasia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotadasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotadasiaperispomeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotadasiavaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotamacron')
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Imacron', right='Imacron')

x = ugi('Iotaoxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotapsili')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotapsilioxia')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotapsiliperispomeni')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotapsilivaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotavaria')
x.addKerning(left='Omegadasiavaria', right='Eta')
x.addMetrics(left='=0', right='Iota')

x = ugi('Iotavrachy')
x.addKerning(left='Eta', right='Eta')
x.addMetrics(left='Ibreve', right='Ibreve')

x = ugi('Omegadasia')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaoxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaoxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegadasiaoxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegadasiaperispomeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegadasiaperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegadasiavaria')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiavariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiavariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegadasiavariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegadasiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegadasiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegadasiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegaoxia')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsili')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsilioxia')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsilioxiaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsilioxiaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegapsilioxiaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegapsiliperispomeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsiliperispomeniypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsiliperispomeniypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegapsiliperispomeniypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegapsilivaria')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsilivariaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsilivariaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegapsilivariaypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegapsiliypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegapsiliypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegapsiliypogegrammeni.ss03')
x.addMetrics(left='=0', right='iota')

x = ugi('Omegavaria')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='=0', right='Omega')

x = ugi('Omegaypogegrammeni')
x.addKerning(left='Omegadasiavaria', right='Omega')
x.addMetrics(left='Omega', right='Omega')

x = ugi('Omegaypogegrammeni.ss01')
x.addKerning(left='Omegadasiavaria', right='iota')

x = ugi('Omegaypogegrammeni.ss03')
x.addMetrics(left='Omega', right='iota')

x = ugi('Omicrondasia')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicrondasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicrondasiavaria')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicronoxia')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicronpsili')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicronpsilioxia')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicronpsilivaria')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Omicronvaria')
x.addKerning(left='Omegadasiavaria', right='Omicron')
x.addMetrics(left='=0', right='Omicron')

x = ugi('Rhodasia')
x.addKerning(left='Omegadasiavaria', right='Rho')
x.addMetrics(left='=0', right='Rho')

x = ugi('Upsilondasia')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilondasiaoxia')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilondasiaperispomeni')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilondasiavaria')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilonmacron')
x.addKerning(left='Upsilon', right='Upsilon')
x.addMetrics(left='Upsilon', right='Upsilon')

x = ugi('Upsilonoxia')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilonvaria')
x.addKerning(left='Omegadasiavaria', right='Upsilon')
x.addMetrics(left='=0', right='Upsilon')

x = ugi('Upsilonvrachy')
x.addKerning(left='Upsilon', right='Upsilon')
x.addMetrics(left='Upsilon', right='Upsilon')

x = ugi('alphadasia')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiaoxia')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiaoxiaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiaperispomeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiaperispomeniypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiavaria')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiavariaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphadasiaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphamacron')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphaoxia')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphaoxiaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphaperispomeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphaperispomeniypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsili')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsilioxia')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsilioxiaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsiliperispomeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsiliperispomeniypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsilivaria')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsilivariaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphapsiliypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphavaria')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphavariaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphavrachy')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('alphaypogegrammeni')
x.addKerning(left='omicron', right='alpha')
x.addMetrics(left='alpha', right='alpha')

x = ugi('epsilondasia')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilondasiaoxia')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilondasiavaria')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilonoxia')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilonpsili')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilonpsilioxia')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilonpsilivaria')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('epsilonvaria')
x.addKerning(left='epsilon', right='epsilon')
x.addMetrics(left='epsilon', right='epsilon')

x = ugi('etadasia')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiaoxia')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiaoxiaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiaperispomeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiaperispomeniypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiavaria')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiavariaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etadasiaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etaoxia')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etaoxiaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etaperispomeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etaperispomeniypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsili')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsilioxia')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsilioxiaypogegrammeni')
x.addRecipe('eta', 'psilioxia', 'ypogegrammenicomb')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsiliperispomeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsiliperispomeniypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsilivaria')
x.addRecipe('eta', 'psilivaria')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsilivariaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etapsiliypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etavaria')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etavariaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('etaypogegrammeni')
x.addKerning(left='eta', right='eta')
x.addMetrics(left='eta', right='eta')

x = ugi('iotadasia')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotatonos', right='iotatonos')

x = ugi('iotadasiaoxia')
x.addKerning(left='iotadieresistonos', right='iotadieresistonos')
x.addMetrics(left='iotadieresistonos', right='iotadieresistonos')

x = ugi('iotadasiaperispomeni')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotadasiavaria')
x.addKerning(left='iotadieresistonos', right='iotadieresistonos')
x.addMetrics(left='iotadieresistonos', right='iotadieresistonos')

x = ugi('iotadialytikaoxia')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotadialytikaperispomeni')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotadialytikavaria')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotamacron')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotaoxia')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotatonos', right='iotatonos')

x = ugi('iotaperispomeni')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotapsili')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotatonos', right='iotatonos')

x = ugi('iotapsilioxia')
x.addKerning(left='iotadieresistonos', right='iotadieresistonos')
x.addMetrics(left='iotadieresistonos', right='iotadieresistonos')

x = ugi('iotapsiliperispomeni')
x.addKerning(left='iota', right='iota')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('iotapsilivaria')
x.addKerning(left='iotadieresistonos', right='iotadieresistonos')
x.addMetrics(left='iotadieresistonos', right='iotadieresistonos')

x = ugi('iotavaria')
x.addKerning(left='iotadieresis', right='iota')
x.addMetrics(left='iotatonos', right='iotatonos')

x = ugi('iotavrachy')
x.addKerning(left='iotadieresis', right='iotadieresis')
x.addMetrics(left='iotadieresis', right='iotadieresis')

x = ugi('omegadasia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiaoxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiaoxiaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiaperispomeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiaperispomeniypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiavaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiavariaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegadasiaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegaoxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegaoxiaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegaperispomeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegaperispomeniypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsili')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsilioxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsilioxiaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsiliperispomeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsiliperispomeniypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsilivaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsilivariaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegapsiliypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegavaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegavariaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omegaypogegrammeni')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicrondasia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicrondasiaoxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicrondasiavaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicronoxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicronpsili')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicronpsilioxia')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicronpsilivaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('omicronvaria')
x.addKerning(left='omicron', right='omicron')
x.addMetrics(left='omicron', right='omicron')

x = ugi('rhodasia')
x.addKerning(left='rho', right='omicron')
x.addMetrics(left='rho', right='omicron')

x = ugi('rhopsili')
x.addKerning(left='rho', right='omicron')
x.addMetrics(left='rho', right='omicron')

x = ugi('upsilondasia')
x.addKerning(left='upsilon', right='upsilondieresistonos')
x.addMetrics(left='upsilon', right='upsilondieresistonos')

x = ugi('upsilondasiaoxia')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondasiaperispomeni')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondasiavaria')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondialytikaoxia')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondialytikaperispomeni')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilondialytikavaria')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonmacron')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonoxia')
x.addKerning(left='upsilon', right='upsilondieresistonos')
x.addMetrics(left='upsilon', right='upsilondieresistonos')

x = ugi('upsilonperispomeni')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonpsili')
x.addKerning(left='upsilon', right='upsilondieresistonos')
x.addMetrics(left='upsilon', right='upsilondieresistonos')

x = ugi('upsilonpsilioxia')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonpsiliperispomeni')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonpsilivaria')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('upsilonvaria')
x.addKerning(left='upsilon', right='upsilondieresistonos')
x.addMetrics(left='upsilon', right='upsilondieresistonos')

x = ugi('upsilonvrachy')
x.addKerning(left='upsilondieresistonos', right='upsilondieresistonos')
x.addMetrics(left='upsilondieresistonos', right='upsilondieresistonos')

x = ugi('alphadasia.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiaoxia.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiaoxiaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiaperispomeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiaperispomeniypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiavaria.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiavariaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphadasiaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphamacron.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphaoxia.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsili.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsilioxia.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsilioxiaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsiliperispomeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsiliperispomeniypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsilivaria.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsilivariaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphapsiliypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphavaria.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphavrachy.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('alphaypogegrammeni.sc')
x.addKerning(left='alpha.sc', right='alpha.sc')
x.addMetrics(left='alpha.sc', right='alpha.sc')

x = ugi('epsilondasia.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilondasiaoxia.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilondasiavaria.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilonoxia.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilonpsili.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilonpsilioxia.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilonpsilivaria.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('epsilonvaria.sc')
x.addKerning(left='eta.sc', right='epsilon.sc')
x.addMetrics(left='eta.sc', right='epsilon.sc')

x = ugi('etadasia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiaoxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiaoxiaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiaperispomeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiaperispomeniypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiavaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiavariaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etadasiaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etaoxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsili.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsilioxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsilioxiaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsiliperispomeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsiliperispomeniypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsilivaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsilivariaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etapsiliypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etavaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('etaypogegrammeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotadasia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotadasiaoxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotadasiaperispomeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotadasiavaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotamacron.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotaoxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotapsili.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotapsilioxia.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotapsiliperispomeni.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotapsilivaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotavaria.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('iotavrachy.sc')
x.addKerning(left='eta.sc', right='eta.sc')
x.addMetrics(left='eta.sc', right='eta.sc')

x = ugi('omegadasia.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiaoxia.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiaoxiaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiaperispomeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiaperispomeniypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiavaria.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiavariaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegadasiaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegaoxia.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsili.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsilioxia.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsilioxiaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsiliperispomeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsiliperispomeniypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsilivaria.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsilivariaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegapsiliypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegavaria.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omegaypogegrammeni.sc')
x.addKerning(left='omega.sc', right='omega.sc')
x.addMetrics(left='omega.sc', right='omega.sc')

x = ugi('omicrondasia.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicrondasiaoxia.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicrondasiavaria.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicronoxia.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicronpsili.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicronpsilioxia.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicronpsilivaria.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('omicronvaria.sc')
x.addKerning(left='omicron.sc', right='omicron.sc')
x.addMetrics(left='omicron.sc', right='omicron.sc')

x = ugi('rhodasia.sc')
x.addKerning(left='eta.sc', right='rho.sc')
x.addMetrics(left='eta.sc', right='rho.sc')

x = ugi('upsilondasia.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilondasiaoxia.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilondasiaperispomeni.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilondasiavaria.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilonmacron.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilonoxia.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilonvaria.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')

x = ugi('upsilonvrachy.sc')
x.addKerning(left='upsilon.sc', right='upsilon.sc')
x.addMetrics(left='upsilon.sc', right='upsilon.sc')