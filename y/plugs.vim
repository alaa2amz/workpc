" --- Vim-Plug Initialization ---
call plug#begin('~/.vim_runtime/plugged')

" Navigation & File Management
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
Plug 'preservim/nerdtree'

" Core Editing Power
Plug 'tpope/vim-surround'
Plug 'tpope/vim-commentary'
Plug 'tpope/vim-repeat'

" Code Intelligence & Auto-formatting for Python
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'psf/black', { 'branch': 'stable' }

" Git Integration
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'

" Visuals & Status Lines
Plug 'vim-airline/vim-airline'

call plug#end()

" --- Quick Configuration Blocks ---

" 1. Auto-format Python files on save using Black
autocmd BufWritePre *.py execute ':Black'

" 2. Practical Keymaps
nnoremap <C-n> :NERDTreeToggle<CR>
nnoremap <C-p> :Files<CR>
