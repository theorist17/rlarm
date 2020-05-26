
import pybullet

class Simulator():
    def __init__(self):

        pybullet.connect(pybullet.GUI)

        pybullet.resetSimulation()

        import pybullet_data
        pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())

        plane = pybullet.loadURDF("plane.urdf")

        robot = pybullet.loadURDF("../res/kuka_kr210_support/urdf/kr210l150.urdf",
                                  [0, 0, 0], useFixedBase=1)
        position, orientation = pybullet.getBasePositionAndOrientation(robot)

        pybullet.getNumJoints(robot)

        joint_index = 2
        joint_info = pybullet.getJointInfo(robot, joint_index)
        name, joint_type, lower_limit, upper_limit = \
            joint_info[1], joint_info[2], joint_info[8], joint_info[9]

        joint_positions = [j[0] for j in pybullet.getJointStates(robot, range(6))]

        world_position, world_orientation = pybullet.getLinkState(robot, 2)[:2]
        pybullet.setGravity(0, 0, -9.81)   # everything should fall down
        pybullet.setTimeStep(0.0001)       # this slows everything down, but let's be accurate...
        pybullet.setRealTimeSimulation(0)  # we want to be faster than real time :)

        pybullet.setJointMotorControlArray(
            robot, range(6), pybullet.POSITION_CONTROL, targetPositions=[0.1] * 6)

    def __del__(self):
        pybullet.disconnect()

    def run(self):
        for _ in range(100000):
            pybullet.stepSimulation()



if __name__=='__main__':
    sim = Simulator()
    sim.run()