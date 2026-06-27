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
let g:ale_completion_enabled = 1

" Allow ALE to auto-import modules/components upon completion
let g:ale_completion_autoimport = 1

set completeopt=menuone,noinsert,noselect,popup
let g:ale_hover_to_floating_preview = 1
source $HOME/ale-map.vim
