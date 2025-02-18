import re
from nicegui import ui
from solver import BookwormSolver

solver = BookwormSolver()

@ui.page('/')
async def main():
    await solver.load_all_dictionaries()
    
    def on_submit(letters: str):
        # Sanitize input: remove spaces, numbers, and special characters
        sanitized_letters = re.sub(r'[^a-zA-Z]', '', letters)
        
        if not sanitized_letters:
            ui.notify('Please enter letters')
            return
            
        # if len(sanitized_letters) != 16:
        #     ui.notify('Please enter exactly 16 letters')
        #     return
            
        solutions = solver.find_solutions(sanitized_letters)
        
        # Clear previous results
        results_container.clear()
        
        with results_container:
            # Create tabs for each dictionary
            with ui.tabs().classes('w-full') as tabs:
                for filename in solutions:
                    ui.tab(filename, filename)
                    
            with ui.tab_panels(tabs, value=next(iter(solutions))).classes('w-full'):
                for filename, words in solutions.items():
                    with ui.tab_panel(filename):
                        columns = [
                            {'name': 'word', 'label': 'Word', 'field': 'word'},
                            {'name': 'strength', 'label': 'Strength', 'field': 'strength'}
                        ]
                        rows = [{'word': word, 'strength': f"{strength:.1f}"} 
                               for word, strength in words]
                        ui.table(columns=columns, rows=rows, row_key='word').classes('w-full')

    ui.add_head_html('''
        <style>
        .custom-input { font-size: 1.2em; padding: 0.5em; width: 100%; }
        </style>
    ''')
    
    with ui.column().classes('w-full max-w-3xl mx-auto p-4 gap-4'):
        ui.label('Bookworm Solver').classes('text-2xl font-bold')
        ui.label('Enter 16 letters:').classes('text-lg')
        
        with ui.row().classes('w-full items-center gap-2'):
            input_field = ui.input('Letters').classes('custom-input flex-grow')
            ui.button('Find Words', on_click=lambda: on_submit(input_field.value))
            
        results_container = ui.column().classes('w-full')

ui.run(title='Bookworm Solver', native=True)
