import pygame
from box import Box
from constants import *
from preferences import Preferences
from time import sleep

pref = Preferences()

pygame.init()
pygame.font.init()
font = pygame.font.SysFont(pref.font_family, pref.font_size)

display_res = display_sizes[pref.user_resolution]
display = pygame.display.set_mode(display_res)


def draw_home():
    while 1:
        display.fill(colors["white"])
        display_width, display_height = display_res
        menu_width = display_width * 0.6
        menu_height = display_height * 0.6
        menu_options = ["Start", "Settings", "Exit"]
        pygame.draw.rect(
            surface=display,
            color=colors["green"],
            rect=pygame.Rect(
                (
                    (display_width - menu_width) // 2,
                    (display_height - menu_height) // 2,
                ),
                (menu_width, menu_height),
            ),
            width=5,
        )
        hitboxes = []
        for i, option in enumerate(menu_options):
            text = font.render(option, True, colors["black"], colors["white"])
            text_width = text.get_width()
            text_height = text.get_height() + 10
            point_x = (display_width - text_width) // 2
            point_y = (
                display_height - text_height * len(menu_options)
            ) // 2 + i * text_height
            hitboxes.append(
                (
                    (
                        point_x,
                        point_y,
                    ),
                    (
                        point_x + text_width,
                        point_y + text_height,
                    ),
                )
            )
            display.blit(
                text,
                (
                    point_x,
                    point_y,
                ),
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # hitboxes[x] is the menu option
                    # hitboxes[][x] is the top left corner of the hitbox as cords(x1,y1)
                    # hitboxes[][][x] is the bottom right corner of the hitbox as cords(x2,y2)
                    if (
                        hitboxes[0][0][0] < event.pos[0] < hitboxes[0][1][0]
                        and hitboxes[0][0][1] < event.pos[1] < hitboxes[0][1][1]
                    ):
                        draw_game()
                    if (
                        hitboxes[1][0][0] < event.pos[0] < hitboxes[1][1][0]
                        and hitboxes[1][0][1] < event.pos[1] < hitboxes[1][1][1]
                    ):
                        draw_settings()
                    if (
                        hitboxes[2][0][0] < event.pos[0] < hitboxes[2][1][0]
                        and hitboxes[2][0][1] < event.pos[1] < hitboxes[2][1][1]
                    ):
                        pygame.quit()
                        quit()

        pygame.display.flip()
        sleep(0.01)


def draw_settings():

    def draw_popup(popup_options):
        while 1: 
            options = len(popup_options) + 1
            popup_height = 50 * options
            popup_width = display_width * 0.4
            pygame.draw.rect(
                surface=display,
                color=colors["red"],
                rect=pygame.Rect(
                    (
                        (display_width - popup_width) // 2,
                        (display_height - popup_height) // 2,
                    ),
                    (popup_width, popup_height),
                ),
                width=5,
            )
            # hitboxes = []
            # for i, option in enumerate(popup_options):
            #     text = font.render(option, True, colors["black"], colors["white"])
            #     text_width = text.get_width()
            #     text_height = text.get_height() + 10
            #     point_x = (display_width - text_width) // 2
            #     point_y = (
            #         display_height - text_height * len(menu_options)
            #     ) // 2 + i * text_height
            #     hitboxes.append(
            #         (
            #             (
            #                 point_x,
            #                 point_y,
            #             ),
            #             (
            #                 point_x + text_width,
            #                 point_y + text_height,
            #             ),
            #         )
            #     )
            #     display.blit(
            #         text,
            #         (
            #             point_x,
            #             point_y,
            #         ),
            #     )
            # pygame.display.flip()
            # sleep(5)

    while 1:
        display.fill(colors["white"])
        display_width, display_height = display_res
        menu_width = display_width * 0.6
        menu_height = display_height * 0.6
        menu_options = [
            "Difficulty",
            "Resolution",
            "Save History",
            "Font Family",
            "Font Size",
            "Back",
        ]
        pygame.draw.rect(
            surface=display,
            color=colors["green"],
            rect=pygame.Rect(
                (
                    (display_width - menu_width) // 2,
                    (display_height - menu_height) // 2,
                ),
                (menu_width, menu_height),
            ),
            width=5,
        )
        hitboxes = []
        for i, option in enumerate(menu_options):
            text = font.render(option, True, colors["black"], colors["white"])
            text_width = text.get_width()
            text_height = text.get_height() + 10
            point_x = (display_width - text_width) // 2
            point_y = (
                display_height - text_height * len(menu_options)
            ) // 2 + i * text_height
            hitboxes.append(
                (
                    (
                        point_x,
                        point_y,
                    ),
                    (
                        point_x + text_width,
                        point_y + text_height,
                    ),
                )
            )
            display.blit(
                text,
                (
                    point_x,
                    point_y,
                ),
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # hitboxes[x] is the menu option
                    # hitboxes[][x] is the top left corner of the hitbox as cords(x1,y1)
                    # hitboxes[][][x] is the bottom right corner of the hitbox as cords(x2,y2)
                    if (
                        hitboxes[0][0][0] < event.pos[0] < hitboxes[0][1][0]
                        and hitboxes[0][0][1] < event.pos[1] < hitboxes[0][1][1]
                    ):
                        draw_popup(difficulty_options)
                    if (
                        hitboxes[1][0][0] < event.pos[0] < hitboxes[1][1][0]
                        and hitboxes[1][0][1] < event.pos[1] < hitboxes[1][1][1]
                    ):
                        pass
                    if (
                        hitboxes[2][0][0] < event.pos[0] < hitboxes[2][1][0]
                        and hitboxes[2][0][1] < event.pos[1] < hitboxes[2][1][1]
                    ):
                        pygame.quit()
                        quit()

        pygame.display.flip()
        sleep(0.01)


def draw_game():
    target_size = target_sizes[pref.difficulty]
    box = Box(
        color=colors["green"],
        point=(
            (display.get_width() - target_size) // 2,
            (display.get_height() - target_size) // 2,
        ),
        size=(target_size, target_size),
        s_time=pygame.time.get_ticks(),
        duration=durations[pref.difficulty] * 1000,
        side_len=target_size,
        display_res=display_res,
    )
    display.fill(colors["white"])
    while 1:
        if not (pref.save_history):
            display.fill(colors["white"])
        box.draw(display)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (
                        box.point[0] < event.pos[0] < box.point[0] + box.size[0]
                        and box.point[1] < event.pos[1] < box.point[1] + box.size[1]
                    ):
                        box.hitcount += 1
                        box.score += 1
                        box.shift_pos()
        box.interpolate_color()

        font.set_bold(True)
        text = font.render(
            f"Score: {box.score}", True, colors["black"], colors["white"]
        )
        display.blit(text, (10, 10))
        font.set_bold(False)

        text = font.render(
            f"Hits: {box.hitcount}", True, colors["black"], colors["white"]
        )
        display.blit(text, (10, 10 + font.get_height()))

        text = font.render(
            f"Miss: {box.hitcount - box.score}", True, colors["black"], colors["white"]
        )
        display.blit(text, (10, 10 + font.get_height() * 2))

        pygame.display.flip()
        sleep(0.01)


def main():
    # draw_game()
    draw_home()


main()
