 local M = {}

function M.setup()
  require('base16-colorscheme').setup({
    base00 = '#000000',
    base01 = '#131314',
    base02 = '#1e1e1f',
    base03 = '#8e9196',
    base04 = '#c5c6cc',
    base05 = '#e4e2e3',
    base06 = '#e4e2e3',
    base07 = '#e4e2e3',
    base08 = '#ffb4ab',
    base09 = '#d4c1d2',
    base0A = '#c4c6cd',
    base0B = '#bdc7d6',
    base0C = '#d4c1d2',
    base0D = '#bdc7d6',
    base0E = '#c4c6cd',
    base0F = '#e0e2e9',
  })

  local hi = function(group, opts)
    vim.api.nvim_set_hl(0, group, opts)
  end

  -- telescope.nvim
  hi('TelescopeNormal',         { fg = '#e4e2e3',          bg = '#000000' })
  hi('TelescopeBorder',         { fg = '#8e9196',             bg = '#000000' })
  hi('TelescopePromptNormal',   { fg = '#e4e2e3',          bg = '#000000' })
  hi('TelescopePromptBorder',   { fg = '#8e9196',             bg = '#000000' })
  hi('TelescopePromptPrefix',   { fg = '#bdc7d6',             bg = '#000000' })
  hi('TelescopePromptCounter',  { fg = '#c5c6cc',  bg = '#000000' })
  hi('TelescopePromptTitle',    { fg = '#000000',             bg = '#bdc7d6' })
  hi('TelescopePreviewTitle',   { fg = '#000000',             bg = '#c4c6cd' })
  hi('TelescopeResultsTitle',   { fg = '#000000',             bg = '#d4c1d2' })
  hi('TelescopeSelection',      { fg = '#e4e2e3',          bg = '#1e1e1f' })
  hi('TelescopeSelectionCaret', { fg = '#bdc7d6',             bg = '#1e1e1f' })
  hi('TelescopeMatching',       { fg = '#bdc7d6',             bold = true })

  -- mini.pick
  hi('MiniPickNormal',         { fg = '#e4e2e3',          bg = '#000000' })
  hi('MiniPickBorder',         { fg = '#8e9196',             bg = '#000000' })
  hi('MiniPickPrompt',   { fg = '#e4e2e3',          bg = '#000000' })
  hi('MiniPickPromptPrefix',   { fg = '#bdc7d6',             bg = '#000000' })
  hi('MiniPickBorderText',    { fg = '#000000',             bg = '#bdc7d6' })
  hi('MiniPickMatchCurrent',      { fg = '#e4e2e3',          bg = '#1e1e1f' })
  hi('MiniPickPromptCaret', { fg = '#bdc7d6',             bg = '#1e1e1f' })
  hi('MiniPickMatchRanges',       { fg = '#bdc7d6',             bold = true })
end

-- Register a signal handler for SIGUSR1 (matugen updates).
-- The handler re-requires this module, which re-runs the code below, so the
-- previous handle is stopped first; otherwise handlers double on every signal.
if _G.__matugen_signal then
  _G.__matugen_signal:stop()
  _G.__matugen_signal:close()
end

local signal = vim.uv.new_signal()
_G.__matugen_signal = signal
signal:start(
  'sigusr1',
  vim.schedule_wrap(function()
    package.loaded['matugen'] = nil
    require('matugen').setup()
  end)
)

return M
