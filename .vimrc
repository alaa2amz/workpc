source $VIMRUNTIME/vimrc_example.vim
"source $HOME/py.vim
set background=dark
colorscheme torte

"set t_ti= t_te=
"set wildmenu      " Visual menu for command-line completion
autocmd InsertLeave * pclose
"set wildmode=list:longest,full  " Set how completion cycles through matches
"set completeopt=menuone,noinsert,noselect,popup
"" Enable filetype plugins
"filetype plugin on
"nnoremap <silent> <space> :nohlsearch<CR>
nnoremap <silent> <Esc> :nohlsearch<CR>


"" Set up JavaScript omni completion explicitly (optional, Vim usually handles this automatically)
"autocmd FileType javascript setlocal omnifunc=javascriptcomplete#Complete

""""""""""
"packadd! ale
"" Enable completion
let g:ale_completion_enabled = 1
"" Allow ALE to auto-import modules/components upon completion
"source $HOME/ale-map.vim
set omnifunc=ale#completion#OmniFunc
""" Map Ruff rule prefixes to correct ALE severities
"let g:ale_type_map = {
"\   'ruff': {
"\       'E': 'E',
"\       'W': 'W',
"\       'I': 'INFO',
"\       'F401': 'W',
"\   }
"\}

"" Force ALE to treat Ruff's F821 (undefined name) and other critical issues as errors
"let g:ale_python_ruff_change_exceptions = 1
"let g:ale_type_map = {
"\   'ruff': {
"\       'E': 'E',
"\       'F': 'E',
"\       'W': 'W',
"\       'F821': 'E',
"\   }
"\}

" Force ALE to treat all ruff outputs as errors
let g:ale_python_ruff_options = '--select=E,F'
let g:ale_type_map = {'ruff': {'W': 'W', 'I': 'I', 'E': 'E'}}
let g:ale_completion_enabled = 1
let g:ale_lsp_suggestions = 1





""""""""""
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()

Plug 'stephpy/vim-yaml' " High-quality YAML syntax package if needed
"Plug 'girishji/vimcomplete'
" List your plugins here
"Plug 'tpope/vim-sensible'

Plug 'neoclide/coc.nvim', {'branch': 'release'}
"Plug 'dense-analysis/ale'

"if has('nvim')
"  Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
"else
"  Plug 'Shougo/deoplete.nvim'
"  Plug 'roxma/nvim-yarp'
"  Plug 'roxma/vim-hug-neovim-rpc'
"endif

call plug#end()




"let g:deoplete#enable_at_startup = 1
source $HOME/.vim/plugged/coc.nvim/doc/coc-example-config.vim 
"set omnifunc=ale#completion#OmniFunc

map \s i_<Esc>l~<Esc>
map \r :w<bar>!python3 %<CR>
vmap <C-c> "+y


" Enable ALE completion features
"let g:ale_completion_enabled = 0

" Set up a Python LSP linter (e.g., pylsp)
let g:ale_linters = {
    \ 'python': ['pylint'],
    \ }

" Ensure completion options show preview/menu details nicely





"""""" Clear current syntax lock if needed
"""""unlet! b:current_syntax
"""""
"""""" Include YAML syntax group
"""""syntax include @YAML syntax/yaml.vim
"""""
"""""" Define a region that triggers on a specific identifier or comment prefix, e.g. yaml: or #yaml
"""""syntax region yamlPythonString matchgroup=SpecialComment
"""""      \ start=/\z('''\|"""\)\_s*\(#\s*yaml\|yaml:\)/
"""""      \ end=/\z1/
"""""      \ contains=@YAML
"""""
"""""let b:current_syntax = 'python'

"call plug#begin('~/.vim/plugged')
" Your other plugins...
"Plug 'stephpy/vim-yaml' " High-quality YAML syntax package if needed
"call plug#end()

" --- Embedded YAML in Python Triple Quotes ---

augroup PythonYamlString
  autocmd!
  " Trigger the syntax injection whenever a Python file is loaded
  autocmd FileType python
        \ unlet! b:current_syntax |
        \ syntax include @YAML syntax/yaml.vim |
        \ syntax region yamlPythonString matchgroup=SpecialComment
        \ start=/\z('''\|"""\)\_s*\(#\s*yaml\|yaml:\)/
        \ end=/\z1/
        \ contains=@YAML |
        \ let b:current_syntax = 'python'
augroup END

