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

set background=dark
colorscheme torte

autocmd InsertLeave * pclose
"nnoremap <silent> <space> :nohlsearch<CR>
nnoremap <silent> <Esc> :nohlsearch<CR>

" Force ALE to treat all ruff outputs as errors
let g:ale_python_ruff_options = '--select=E,F'
let g:ale_type_map = {'ruff': {'W': 'W', 'I': 'I', 'E': 'E'}}
let g:ale_completion_enabled = 0
let g:ale_lsp_suggestions = 0
let g:ale_enabled = 0
"source $HOME/ale-map.vim
"set omnifunc=ale#completion#OmniFunc

source $HOME/.vim/plugged/coc.nvim/doc/coc-example-config.vim 

map \s i_<Esc>l~<Esc>
map \r :w<bar>!python3 %<CR>
vmap <C-c> "+y
map \at :ALEToggle<CR>
map \cd :CocDisable<CR>
map \ce :CocEnable<CR>
nmap <F8> :TagbarToggle<CR>

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

autocmd FileType python setlocal formatprg=black\ -q\ 2>/dev/null\ --stdin-filename\ %\ -

"set t_ti= t_te=
"set wildmenu      " Visual menu for command-line completion
"set wildmode=list:longest,full  " Set how completion cycles through matches
"set completeopt=menuone,noinsert,noselect,popup
"" Enable filetype plugins
"filetype plugin on
"Plug 'girishji/vimcomplete'
" List your plugins here
