set runtimepath^=~/.vim runtimepath+=~/.vim/after
set termguicolors
let &packpath = &runtimepath
lua require('plugins')
lua require('colorizer').setup()
lua require('nvim-tree').setup {}
lua require('feline').setup()
let mapleader=","
nnoremap('<leader>fu', 'Telescope lsp_references')
nnoremap('<leader>gd', 'Telescope lsp_definitions')
nnoremap('<leader>rn', 'lua vim.lsp.buf.rename()')
nnoremap('<leader>dn', 'lua vim.lsp.diagnostic.goto_next()')
nnoremap('<leader>dN', 'lua vim.lsp.diagnostic.goto_prev()')
nnoremap('<leader>dd', 'Telescope lsp_document_diagnostics')
nnoremap('<leader>dD', 'Telescope lsp_workspace_diagnostics')
nnoremap('<leader>xx', 'Telescope lsp_code_actions')
nnoremap('<leader>xd', '%Telescope lsp_range_code_actions')
source ~/.vimrc

