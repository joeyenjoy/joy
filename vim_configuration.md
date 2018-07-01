"annotation is started with "

set nu   "show line number
set cursorline "show cursor linewise
set cursorcolumn  "shwo cursor columnwise
set ts=4  "set tab space
set shiftwidth=4 "set shift space
set expandtab "change tab to sapce

syntax enable
syntax on

map <F5> :call RunPython()<CR>
func! RunPython()
    exec "W"
    if &filetype == 'python'
        exec "!time python2.7 %"
    endif
endfunc
  
  
colorscheme darkblue
