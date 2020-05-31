import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'  # center whole window position
pygame.init()
WIDTH = 800
HEIGHT = 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Binary tree visualizer")
CLOCK = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 20)


class Node:

    def __init__(self, left, right, level):
        self.left = left
        self.right = right
        self.level = level


node_number = 0


def visit(node):
    global node_number
    node_number += 1
    node.number = node_number
    text = font.render("{}".format(node.number), True, (255, 255, 255))
    WIN.blit(text, (int(node.number * 50), int(node.level * 50)))
    pygame.display.update()


def visualize_nodes(node):
    if node.left is not None:
        visualize_nodes(node.left)
    visit(node)
    if node.right is not None:
        visualize_nodes(node.right)


visited_nodes = []


def walk_depth_first(node):
    visited_nodes.append(node)
    if node is None or (node.right is None and node.left is None):
        return
    if node.left is not None:
        walk_depth_first(node.left)
    if node.right is not None:
        walk_depth_first(node.right)


def visualize_branches(nodes):
    for i in range(0, len(nodes)):
        if i + 1 < len(nodes):
            x1 = nodes[i].number * 50
            y1 = nodes[i].level * 50
            x2 = nodes[i + 1].number * 50
            y2 = nodes[i + 1].level * 50
            pygame.draw.line(WIN, (255, 255, 255), (x1, y1), (x2, y2))
            pygame.display.update()


def visualize_tree(node):
    visualize_nodes(node)
    walk_depth_first(node)
    visualize_branches(visited_nodes)  # not working to be fixed


def main():
    tree = Node(
        Node(
            Node(
                Node(None, None, 4.0), None, 3.0),
            Node(None, None, 3.0),
            2.0),
        Node(
            Node(None, None, 3.0), None, 2.0),
        1.0)
    visualize_tree(tree)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


if __name__ == '__main__':
    main()
