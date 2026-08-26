source $VIMRUNTIME/vimrc_example.vim

"auto install plug
let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()

Plug 'stephpy/vim-yaml' " High-quality YAML syntax package if needed
Plug 'tpope/vim-sensible'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'dense-analysis/ale'
Plug 'preservim/tagbar'
Plug 'liuchengxu/vista.vim'


call plug#end()
ALEDisable
set background=dark
colorscheme torte

autocmd InsertLeave * pclose
"nnoremap <silent> <space> :nohlsearch<CR>
nnoremap <silent> <Esc> :nohlsearch<CR>



" Force ALE to treat all ruff outputs as errors
let g:ale_python_ruff_options = '--select=E,F'
let g:ale_type_map = {'ruff': {'W': 'W', 'I': 'I', 'E': 'E'}}
let g:ale_completion_enabled = 1
let g:ale_lsp_suggestions = 1
let g:ale_completion_enabled = 1
"source $HOME/ale-map.vim
set omnifunc=ale#completion#OmniFunc










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

"source $HOME/py.vim
"set t_ti= t_te=
"set wildmenu      " Visual menu for command-line completion
"set wildmode=list:longest,full  " Set how completion cycles through matches
"set completeopt=menuone,noinsert,noselect,popup
"" Enable filetype plugins
"filetype plugin on
"Plug 'girishji/vimcomplete'
" List your plugins here
