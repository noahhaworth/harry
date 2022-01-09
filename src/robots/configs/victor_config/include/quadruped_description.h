#ifndef QUADRUPED_DESCRIPTION_H
#define QUADRUPED_DESCRIPTION_H

#include <quadruped_base/quadruped_base.h>

namespace champ
{
    namespace URDF
    {
        void loadFromHeader(champ::QuadrupedBase &base)
        {
      base.lf.hip.setOrigin(0.1125, 0.0475, 0.0, 0.0, 0.0, 0.0);
base.lf.upper_leg.setOrigin(0.0, -0.015, -0.0, 0.0, 0.0, 0.0);
base.lf.lower_leg.setOrigin(0.3, 0.0, -0.1, 0.0, 0.0, 0.0);
     base.lf.foot.setOrigin(0.0, 0.0, -0.102, 0.0, 0.0, 0.0);

      base.rf.hip.setOrigin(0.1125, -0.0475, 0.0, 0.0, 0.0, 0.0);
base.rf.upper_leg.setOrigin(0.0, 0.015, -0.0, 0.0, 0.0, 0.0);
base.rf.lower_leg.setOrigin(0.3, 0.0, -0.1, 0.0, 0.0, 0.0);
     base.rf.foot.setOrigin(0.0, 0.0, -0.102, 0.0, 0.0, 0.0);

      base.lh.hip.setOrigin(-0.1125, 0.0475, 0.0, 0.0, 0.0, 0.0);
base.lh.upper_leg.setOrigin(0.0, -0.015, -0.0, 0.0, 0.0, 0.0);
base.lh.lower_leg.setOrigin(-0.3, 0.0, -0.1, 0.0, 0.0, 0.0);
     base.lh.foot.setOrigin(0.0, 0.0, -0.102, 0.0, 0.0, 0.0);

      base.rh.hip.setOrigin(-0.1125, -0.0475, 0.0, 0.0, 0.0, 0.0);
base.rh.upper_leg.setOrigin(0.0, 0.015, -0.0, 0.0, 0.0, 0.0);
base.rh.lower_leg.setOrigin(-0.3, 0.0, -0.1, 0.0, 0.0, 0.0);
     base.rh.foot.setOrigin(0.0, 0.0, -0.102, 0.0, 0.0, 0.0);
        }
    }
}
#endif