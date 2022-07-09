vim.cmd [[packadd packer.nvim]]

return require('packer').startup(function()
	
	use "wbthomason/packer.nvim"

	use {"lambdalisue/suda.vim"}
	
	use {"ellisonleao/glow.nvim"}

	use {"winseven4lyf/vim-bbcode"}
	
	use {"norcalli/nvim-colorizer.lua"}

	use {"chriskempson/base16-vim"}

	use {"whatyouhide/vim-gotham"}

	use {"morhetz/gruvbox"}

	use {"feline-nvim/feline.nvim"}

	use {"kyazdani42/nvim-web-devicons"}

	use {"danilo-augusto/vim-afterglow"}
	
	use {
		'nvim-telescope/telescope.nvim',
		requires = { { 'nvim-lua/plenary.nvim' } }
	}

	use {
		'kyazdani42/nvim-tree.lua',
	    	requires = {
      			'kyazdani42/nvim-web-devicons',
	    	}
	}
end)

