from position import Position
import pygame

class block:
    def __init__(self):
        self.id = id
        self.cells = {} # the cell blocktiles 
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        
    def move(self, rows, columns):
        self.row_offset += rows
        self.row_offset += columns
    
    def get_cell_positions(self):
        current_cell = self.cells[self.rotation_state]
        moved_cell = []
        # call each block in cells
        for position in current_cell:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_cell.append(position)
        return moved_cell
    
    def rotation(self):
        self.rotation_state += 1
        if self.rotation_state == 4:
            self.rotation_state = 0

    # moving
    def draw(self, screen, posx, posy):
        current_cells = self.get_cell_positions()
        for cell in current_cells:
            cell_rect = pygame.Rect(posx + cell.column * self.cell_size
                                    , posy + cell.row * self.cell_size
                                    , self.cell_size -1, self.cell_size-1)
            pygame.draw.rect(screen, cell_rect)