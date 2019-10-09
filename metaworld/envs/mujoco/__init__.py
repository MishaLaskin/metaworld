import gym
from gym.envs.registration import register
import logging

LOGGER = logging.getLogger(__name__)

_REGISTERED = False


def register_custom_envs():
    global _REGISTERED
    if _REGISTERED:
        return
    _REGISTERED = True

    LOGGER.info("Registering metaworld mujoco gym environments")

    """
    1. Basketball
    """
    def create_state_sawyer_basketball_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_basketball import SawyerBasketballEnv
        env = SawyerBasketballEnv()
        return env

    register(
        id='SawyerBasketballEnv-v1',
        entry_point=create_state_sawyer_basketball_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    2. Bin picking
    """
    def create_state_sawyer_binpicking_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_bin_picking import SawyerBinPickingEnv
        env = SawyerBinPickingEnv()
        return env

    register(
        id='SawyerBinPickingEnv-v1',
        entry_point=create_state_sawyer_binpicking_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    
    """
    3. Box close
    """
    def create_state_sawyer_boxclose_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_box_close import SawyerBoxCloseEnv
        env = SawyerBoxCloseEnv()
        return env

    register(
        id='SawyerBoxCloseEnv-v1',
        entry_point=create_state_sawyer_boxclose_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    
    """
    4. Button press topdown
    """
    def create_state_sawyer_buttonpresstopdown_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_button_press_topdown import SawyerButtonPressTopdownEnv
        env = SawyerButtonPressTopdownEnv()
        return env

    register(
        id='SawyerButtonPressTopdownEnv-v1',
        entry_point=create_state_sawyer_buttonpresstopdown_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    5. Button press topdown wall
    """
    def create_state_sawyer_buttonpresstopdownwall_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_button_press_topdown_wall import SawyerButtonPressTopdownWallEnv
        env = SawyerButtonPressTopdownWallEnv()
        return env

    register(
        id='SawyerButtonPressTopdownWallEnv-v1',
        entry_point=create_state_sawyer_buttonpresstopdownwall_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    6. Button press wall
    """
    def create_state_sawyer_buttonpresswall_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_button_press_wall import SawyerButtonPressWallEnv
        env = SawyerButtonPressWallEnv()
        return env

    register(
        id='SawyerButtonPressWallEnv-v1',
        entry_point=create_state_sawyer_buttonpresswall_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    7. Button press 
    """
    def create_state_sawyer_buttonpress_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_button_press import SawyerButtonPressEnv
        env = SawyerButtonPressEnv()
        return env

    register(
        id='SawyerButtonPressEnv-v1',
        entry_point=create_state_sawyer_buttonpress_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    8. Coffee button  
    """
    def create_state_sawyer_coffeebutton_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_coffee_button import SawyerCoffeeButtonEnv
        env = SawyerCoffeeButtonEnv()
        return env

    register(
        id='SawyerCoffeeButtonEnv-v1',
        entry_point=create_state_sawyer_coffeebutton_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    9. Coffee pull  
    """
    def create_state_sawyer_coffeepull_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_coffee_pull import SawyerCoffeePullEnv
        env = SawyerCoffeePullEnv()
        return env

    register(
        id='SawyerCoffeePullEnv-v1',
        entry_point=create_state_sawyer_coffeepull_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    10. Coffee push  
    """
    def create_state_sawyer_coffeepush_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_coffee_push import SawyerCoffeePushEnv
        env = SawyerCoffeePushEnv()
        return env

    register(
        id='SawyerCoffeePushEnv-v1',
        entry_point=create_state_sawyer_coffeepush_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )


    """
    11. Dial turn 
    """
    def create_state_sawyer_dial_turn_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_dial_turn import SawyerDialTurnEnv
        env = SawyerDialTurnEnv()
        return env

    register(
        id='SawyerDialTurnEnv-v1',
        entry_point=create_state_sawyer_dial_turn_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    12. Disassemble peg 
    """
    def create_state_sawyer_disassemble_peg_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_disassemble_peg import SawyerNutDisassembleEnv
        env = SawyerNutDisassembleEnv()
        return env

    register(
        id='SawyerNutDisassembleEnv-v1',
        entry_point=create_state_sawyer_disassemble_peg_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    13. Close door
    """
    def create_state_sawyer_door_close_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_door_close import SawyerDoorCloseEnv
        env = SawyerDoorCloseEnv()
        return env

    register(
        id='SawyerDoorCloseEnv-v1',
        entry_point=create_state_sawyer_door_close_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    14. Lock door
    """
    def create_state_sawyer_door_lock_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_door_lock import SawyerDoorLockEnv
        env = SawyerDoorLockEnv()
        return env

    register(
        id='SawyerDoorLockEnv-v1',
        entry_point=create_state_sawyer_door_lock_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    15. Unlock door
    """
    def create_state_sawyer_door_unlock_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_door_unlock import SawyerDoorUnlockEnv
        env = SawyerDoorUnlockEnv()
        return env

    register(
        id='SawyerDoorUnlockEnv-v1',
        entry_point=create_state_sawyer_door_unlock_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    16. Door
    """
    def create_state_sawyer_door_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_door import SawyerDoorEnv
        env = SawyerDoorEnv()
        return env

    register(
        id='SawyerDoorEnv-v1',
        entry_point=create_state_sawyer_door_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    17. Drawer Close
    """
    def create_state_sawyer_drawer_close_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_drawer_close import SawyerDrawerCloseEnv
        env = SawyerDrawerCloseEnv()
        return env

    register(
        id='SawyerDrawerCloseEnv-v1',
        entry_point=create_state_sawyer_drawer_close_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    18. Drawer Open
    """
    def create_state_sawyer_drawer_open_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_drawer_open import SawyerDrawerOpenEnv
        env = SawyerDrawerOpenEnv()
        return env

    register(
        id='SawyerDrawerOpenEnv-v1',
        entry_point=create_state_sawyer_drawer_open_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    19. Faucet Open
    """
    def create_state_sawyer_faucet_open_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_faucet_open import SawyerFaucetOpenEnv
        env = SawyerFaucetOpenEnv()
        return env

    register(
        id='SawyerFaucetOpenEnv-v1',
        entry_point=create_state_sawyer_faucet_open_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    20. Faucet Close
    """
    def create_state_sawyer_faucet_close_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_faucet_close import SawyerFaucetCloseEnv
        env = SawyerFaucetCloseEnv()
        return env

    register(
        id='SawyerFaucetCloseEnv-v1',
        entry_point=create_state_sawyer_faucet_close_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    21. Hammer
    """
    def create_state_sawyer_hammer_env_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_hammer import SawyerHammerEnv
        env = SawyerHammerEnv()
        return env

    register(
        id='SawyerHammerEnv-v1',
        entry_point=create_state_sawyer_hammer_env_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    22. Hand insert
    """
    def create_state_sawyer_hand_insert_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_hand_insert import SawyerHandInsertEnv
        env = SawyerHandInsertEnv()
        return env

    register(
        id='SawyerHandInsertEnv-v1',
        entry_point=create_state_sawyer_hand_insert_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    23. Handle press side
    """
    def create_state_sawyer_handle_press_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_handle_press_side import SawyerHandlePressSideEnv
        env = SawyerHandlePressSideEnv()
        return env

    register(
        id='SawyerHandlePressSideEnv-v1',
        entry_point=create_state_sawyer_handle_press_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )


    """
    24. Handle press 
    """
    def create_state_sawyer_handle_press_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_handle_press import SawyerHandlePressEnv
        env = SawyerHandlePressEnv()
        return env

    register(
        id='SawyerHandlePressEnv-v1',
        entry_point=create_state_sawyer_handle_press_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )


    """
    25. Handle pull side 
    """
    def create_state_sawyer_handle_pull_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_handle_pull_side import SawyerHandlePullSideEnv
        env = SawyerHandlePullSideEnv()
        return env

    register(
        id='SawyerHandlePullSideEnv-v1',
        entry_point=create_state_sawyer_handle_pull_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    26. Handle pull  
    """
    def create_state_sawyer_handle_pull_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_handle_pull import SawyerHandlePullEnv
        env = SawyerHandlePullEnv()
        return env

    register(
        id='SawyerHandlePullEnv-v1',
        entry_point=create_state_sawyer_handle_pull_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    27. Lever pull  
    """
    def create_state_sawyer_lever_pull_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_lever_pull import SawyerLeverPullEnv
        env = SawyerLeverPullEnv()
        return env

    register(
        id='SawyerLeverPullEnv-v1',
        entry_point=create_state_sawyer_lever_pull_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    28. Peg insertion side
    """
    def create_state_sawyer_peg_insertion_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_peg_insertion_side import SawyerPegInsertionSideEnv
        env = SawyerPegInsertionSideEnv()
        return env

    register(
        id='SawyerPegInsertionSideEnv-v1',
        entry_point=create_state_sawyer_peg_insertion_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    29. Peg unplug side
    """
    def create_state_sawyer_peg_unplug_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_peg_unplug_side import SawyerPegUnplugSideEnv
        env = SawyerPegUnplugSideEnv()
        return env

    register(
        id='SawyerPegUnplugSideEnv-v1',
        entry_point=create_state_sawyer_peg_unplug_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    30. Pick and place wsg
    """
    def create_state_sawyer_pick_and_place_wsg_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_pick_and_place_wsg import SawyerPickAndPlaceWsgEnv
        env = SawyerPickAndPlaceWsgEnv()
        return env

    register(
        id='SawyerPickAndPlaceWsgEnv-v1',
        entry_point=create_state_sawyer_pick_and_place_wsg_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    31. Pick and place
    """
    def create_state_sawyer_pick_and_place_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_pick_and_place import SawyerPickAndPlaceEnv
        env = SawyerPickAndPlaceEnv()
        return env

    register(
        id='SawyerPickAndPlaceEnv-v1',
        entry_point=create_state_sawyer_pick_and_place_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )


    """
    31. Pick out of hole 
    """
    def create_state_sawyer_pick_out_of_hole_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_pick_out_of_hole import SawyerPickOutOfHoleEnv
        env = SawyerPickOutOfHoleEnv()
        return env

    register(
        id='SawyerPickOutOfHoleEnv-v1',
        entry_point=create_state_sawyer_pick_out_of_hole_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    32. Plate slide back side
    """
    def create_state_sawyer_plate_slide_back_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_plate_slide_back_side import SawyerPlateSlideBackSideEnv
        env = SawyerPlateSlideBackSideEnv()
        return env

    register(
        id='SawyerPlateSlideBackSideEnv-v1',
        entry_point=create_state_sawyer_plate_slide_back_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    """
    33. Plate slide back 
    """
    def create_state_sawyer_plate_slide_back_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_plate_slide_back import SawyerPlateSlideBackEnv
        env = SawyerPlateSlideBackEnv()
        return env

    register(
        id='SawyerPlateSlideBackEnv-v1',
        entry_point=create_state_sawyer_plate_slide_back_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    34. Plate slide side 
    """
    def create_state_sawyer_plate_slide_side_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_plate_slide_side import SawyerPlateSlideSideEnv
        env = SawyerPlateSlideSideEnv()
        return env

    register(
        id='SawyerPlateSlideSideEnv-v1',
        entry_point=create_state_sawyer_plate_slide_side_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    35. Plate slide  
    """
    def create_state_sawyer_plate_slide_v1(*args,**kwargs):
        from metaworld.envs.mujoco.sawyer_xyz.sawyer_plate_slide import SawyerPlateSlideEnv
        env = SawyerPlateSlideEnv()
        return env

    register(
        id='SawyerPlateSlideEnv-v1',
        entry_point=create_state_sawyer_plate_slide_v1,
        tags={
            'git-commit-hash': 'none',
            'author': 'misha'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )
    """
    Reaching tasks
    """

    register(
        id='SawyerReachXYEnv-v1',
        entry_point=create_state_sawyer_reach_xy_env_v1,
        tags={
            'git-commit-hash': '2d95c75',
            'author': 'murtaza'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    register(
        id='SawyerReachXYZEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz.sawyer_reach:SawyerReachXYZEnv',
        tags={
            'git-commit-hash': '7b3113b',
            'author': 'vitchyr'
        },
        kwargs={
            'hide_goal_markers': False,
            'norm_order': 2,
        },
    )

    register(
        id='SawyerReachXYZEnv-v1',
        entry_point='metaworld.envs.mujoco.sawyer_xyz.sawyer_reach:SawyerReachXYZEnv',
        tags={
            'git-commit-hash': 'bea5de',
            'author': 'murtaza'
        },
        kwargs={
            'hide_goal_markers': True,
            'norm_order': 2,
        },
    )

    register(
        id='Image48SawyerReachXYEnv-v1',
        entry_point=create_image_48_sawyer_reach_xy_env_v1,
        tags={
            'git-commit-hash': '2d95c75',
            'author': 'murtaza'
        },
    )
    register(
        id='Image84SawyerReachXYEnv-v1',
        entry_point=create_image_84_sawyer_reach_xy_env_v1,
        tags={
            'git-commit-hash': '2d95c75',
            'author': 'murtaza'
        },
    )


    """
    Pushing Tasks, XY
    """

    register(
        id='SawyerPushAndReachEnvEasy-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': 'ddd73dc',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.15, 0.4, 0.02, -.1, .45),
            goal_high=(0.15, 0.7, 0.02, .1, .65),
            puck_low=(-.1, .45),
            puck_high=(.1, .65),
            hand_low=(-0.15, 0.4, 0.02),
            hand_high=(0.15, .7, 0.02),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck.xml',
            reward_type='state_distance',
            reset_free=False,
            clamp_puck_on_step=True,
        )
    )

    register(
        id='SawyerPushAndReachEnvMedium-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': 'ddd73dc',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.2, 0.35, 0.02, -.15, .4),
            goal_high=(0.2, 0.75, 0.02, .15, .7),
            puck_low=(-.15, .4),
            puck_high=(.15, .7),
            hand_low=(-0.2, 0.35, 0.05),
            hand_high=(0.2, .75, 0.3),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck.xml',
            reward_type='state_distance',
            reset_free=False,
            clamp_puck_on_step=True,
        )
    )

    register(
        id='SawyerPushAndReachEnvHard-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': 'ddd73dc',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.25, 0.3, 0.02, -.2, .35),
            goal_high=(0.25, 0.8, 0.02, .2, .75),
            puck_low=(-.2, .35),
            puck_high=(.2, .75),
            hand_low=(-0.25, 0.3, 0.02),
            hand_high=(0.25, .8, 0.02),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck.xml',
            reward_type='state_distance',
            reset_free=False,
            clamp_puck_on_step=True,
        )
    )

    """
    Pushing tasks, XY, Arena
    """
    register(
        id='SawyerPushAndReachArenaEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': 'dea1627',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.25, 0.3, 0.02, -.2, .4),
            goal_high=(0.25, 0.875, 0.02, .2, .8),
            puck_low=(-.4, .2),
            puck_high=(.4, 1),
            hand_low=(-0.28, 0.3, 0.05),
            hand_high=(0.28, 0.9, 0.3),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck_arena.xml',
            reward_type='state_distance',
            reset_free=False,
        )
    )

    register(
        id='SawyerPushAndReachArenaResetFreeEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': 'dea1627',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.25, 0.3, 0.02, -.2, .4),
            goal_high=(0.25, 0.875, 0.02, .2, .8),
            puck_low=(-.4, .2),
            puck_high=(.4, 1),
            hand_low=(-0.28, 0.3, 0.05),
            hand_high=(0.28, 0.9, 0.3),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck_arena.xml',
            reward_type='state_distance',
            reset_free=True,
        )
    )

    register(
        id='SawyerPushAndReachSmallArenaEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': '7256aaf',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.15, 0.4, 0.02, -.1, .5),
            goal_high=(0.15, 0.75, 0.02, .1, .7),
            puck_low=(-.3, .25),
            puck_high=(.3, .9),
            hand_low=(-0.15, 0.4, 0.05),
            hand_high=(0.15, .75, 0.3),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck_small_arena.xml',
            reward_type='state_distance',
            reset_free=False,
            clamp_puck_on_step=False,
        )
    )

    register(
        id='SawyerPushAndReachSmallArenaResetFreeEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_and_reach_env:SawyerPushAndReachXYEnv',
        tags={
            'git-commit-hash': '7256aaf',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.15, 0.4, 0.02, -.1, .5),
            goal_high=(0.15, 0.75, 0.02, .1, .7),
            puck_low=(-.3, .25),
            puck_high=(.3, .9),
            hand_low=(-0.15, 0.4, 0.05),
            hand_high=(0.15, .75, 0.3),
            norm_order=2,
            xml_path='sawyer_xyz/sawyer_push_puck_small_arena.xml',
            reward_type='state_distance',
            reset_free=True,
            clamp_puck_on_step=False,
        )
    )

    """
    NIPS submission pusher environment
    """
    register(
        id='SawyerPushNIPS-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_nips:SawyerPushAndReachXYEasyEnv',
        tags={
            'git-commit-hash': 'bede25d',
            'author': 'ashvin',
        },
        kwargs=dict(
            hide_goal=True,
            reward_info=dict(
                type="state_distance",
            ),
        )

    )

    register(
        id='SawyerPushNIPSHarder-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_push_nips:SawyerPushAndReachXYHarderEnv',
        tags={
            'git-commit-hash': 'b5cac93',
            'author': 'murtaza',
        },
        kwargs=dict(
            hide_goal=True,
            reward_info=dict(
                type="state_distance",
            ),
        )

    )

    """
    Door Hook Env
    """

    register(
        id='SawyerDoorHookEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_door_hook:SawyerDoorHookEnv',
        tags={
            'git-commit-hash': '15b48d5',
            'author': 'murtaza',
        },
        kwargs = dict(
            goal_low=(-0.1, 0.45, 0.1, 0),
            goal_high=(0.05, 0.65, .25, .83),
            hand_low=(-0.1, 0.45, 0.1),
            hand_high=(0.05, 0.65, .25),
            max_angle=.83,
            xml_path='sawyer_xyz/sawyer_door_pull_hook.xml',
            reward_type='angle_diff_and_hand_distance',
            reset_free=False,
        )
    )

    register(
        id='SawyerDoorHookResetFreeEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_door_hook:SawyerDoorHookEnv',
        tags={
            'git-commit-hash': '15b48d5',
            'author': 'murtaza',
        },
        kwargs=dict(
            goal_low=(-0.1, 0.45, 0.1, 0),
            goal_high=(0.05, 0.65, .25, .83),
            hand_low=(-0.1, 0.45, 0.1),
            hand_high=(0.05, 0.65, .25),
            max_angle=.83,
            xml_path='sawyer_xyz/sawyer_door_pull_hook.xml',
            reward_type='angle_diff_and_hand_distance',
            reset_free=True,
        )
    )

    """
    Pick and Place
    """
    register(
        id='SawyerPickupEnv-v0',
        entry_point='metaworld.envs.mujoco.sawyer_xyz'
                    '.sawyer_pick_and_place:SawyerPickAndPlaceEnv',
        tags={
            'git-commit-hash': '30f23f7',
            'author': 'steven',
        },
        kwargs=dict(
            hand_low=(-0.1, 0.55, 0.05),
            hand_high=(0.0, 0.65, 0.2),
            action_scale=0.02,
            hide_goal_markers=True,
            num_goals_presampled=1000,
        )

    )

    # Sawyer Shelf Reach Env

    register(
        id='SawyerShelfXYZEnv-v1',
        entry_point='metaworld.envs.mujoco.sawyer_xyz.sawyer_shelf_remove:SawyerShelfRemoveEnv',
        tags={
            'git-commit-hash': 'beafc10b3b18b6553bfd3722f76c2095100528ac',
            'author': 'brandon'
        },
        kwargs={
        },
    )

    register(
        id='Image48SawyerShelfXYZEnv-v1',
        entry_point=create_image_48_sawyer_shelf_xy_env_v1,
        tags={
            'git-commit-hash': 'beafc10b3b18b6553bfd3722f76c2095100528ac',
            'author': 'brandon'
        },
    )


def create_image_48_sawyer_shelf_xy_env_v1(**kwargs):
    from metaworld.core.image_env import ImageEnv
    from metaworld.envs.mujoco.cameras import sawyer_door_env_camera_v0

    wrapped_env = gym.make('SawyerShelfXYZEnv-v1', **kwargs)
    return ImageEnv(
        wrapped_env,
        48,
        init_camera=sawyer_door_env_camera_v0,
        transpose=False,
        normalize=True,
    )




def create_state_sawyer_reach_xy_env_v1(*args,**kwargs):
    from metaworld.envs.mujoco.cameras import sawyer_xyz_reacher_camera_v0
    from metaworld.envs.mujoco.sawyer_xyz import SawyerReachPushPickPlaceEnv

    env = SawyerReachPushPickPlaceEnv(task_type='reach')
    return env


def create_image_48_sawyer_reach_xy_env_v1():
    from metaworld.core.image_env import ImageEnv
    from metaworld.envs.mujoco.cameras import sawyer_xyz_reacher_camera_v0
    from metaworld.envs.mujoco.sawyer_xyz import SawyerReachPushPickPlaceEnv

    wrapped_env = SawyerReachPushPickPlaceEnv(task_type='reach')
    return ImageEnv(
        wrapped_env,
        imsize=48,
        init_camera=sawyer_xyz_reacher_camera_v0,
        transpose=True,
        normalize=True,
    )


def create_image_84_sawyer_reach_xy_env_v1():
    from metaworld.core.image_env import ImageEnv
    from metaworld.envs.mujoco.cameras import sawyer_xyz_reacher_camera_v0

    wrapped_env = gym.make('SawyerReachXYEnv-v1')
    return ImageEnv(
        wrapped_env,
        84,
        init_camera=sawyer_xyz_reacher_camera_v0,
        transpose=True,
        normalize=True,
    )

def create_image_48_sawyer_push_and_reach_arena_env_v0():
    from metaworld.core.image_env import ImageEnv
    from metaworld.envs.mujoco.cameras import sawyer_pusher_camera_upright_v2

    wrapped_env = gym.make('SawyerPushAndReachArenaEnv-v0')
    return ImageEnv(
        wrapped_env,
        48,
        init_camera=sawyer_pusher_camera_upright_v2,
        transpose=True,
        normalize=True,
    )

def create_image_48_sawyer_push_and_reach_arena_env_reset_free_v0():
    from metaworld.core.image_env import ImageEnv
    from metaworld.envs.mujoco.cameras import sawyer_pusher_camera_upright_v2

    wrapped_env = gym.make('SawyerPushAndReachArenaResetFreeEnv-v0')
    return ImageEnv(
        wrapped_env,
        48,
        init_camera=sawyer_pusher_camera_upright_v2,
        transpose=True,
        normalize=True,
    )

register_custom_envs()
