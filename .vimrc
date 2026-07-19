set background=dark

source $VIMRUNTIME/vimrc_example.vim

set t_ti= t_te=

set wildmenu      " Visual menu for command-line completion

set wildmode=list:longest,full  " Set how completion cycles through matches

" Enable filetype plugins
"filetype plugin on

" Set up JavaScript omni completion explicitly (optional, Vim usually handles this automatically)
"autocmd FileType javascript setlocal omnifunc=javascriptcomplete#Complete

" Enable completion
"let g:ale_completion_enabled = 0

" Allow ALE to auto-import modules/components upon completion
"let g:ale_completion_autoimport = 0

"set completeopt=menuone,noinsert,noselect,popup
"let g:ale_hover_to_floating_preview = 1
"source $HOME/ale-map.vim

 " set omnifunc=ale#completion#OmniFunc

let data_dir = has('nvim') ? stdpath('data') . '/site' : '~/.vim'
if empty(glob(data_dir . '/autoload/plug.vim'))
  silent execute '!curl -fLo '.data_dir.'/autoload/plug.vim --create-dirs  https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
  autocmd VimEnter * PlugInstall --sync | source $MYVIMRC
endif

call plug#begin()

" List your plugins here
"Plug 'tpope/vim-sensible'

Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()
source $HOME/.vim/plugged/coc.nvim/doc/coc-example-config.vim 
map \s i_<Esc>l~<Esc>
map \pi :w<bar>python3 %<CR>
vmap <C-c> "+y
