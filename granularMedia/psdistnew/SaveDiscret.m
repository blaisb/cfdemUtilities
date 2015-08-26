function fig = SaveDiscret()
% This is the machine-generated representation of a Handle Graphics object
% and its children.  Note that handle values may change when these objects
% are re-created. This may cause problems with any callbacks written to
% depend on the value of the handle at the time the object was saved.
% This problem is solved by saving the output as a FIG-file.
%
% To reopen this object, just type the name of the M-file at the MATLAB
% prompt. The M-file and its associated MAT-file must be on your path.
% 
% NOTE: certain newer features in MATLAB may not have been saved in this
% M-file due to limitations of this format, which has been superseded by
% FIG-files.  Figures which have been annotated using the plot editor tools
% are incompatible with the M-file/MAT-file format, and should be saved as
% FIG-files.

load SaveDiscret

h0 = figure('Units','points', ...
	'Color',[0.8 0.8 0.8], ...
	'Colormap',mat0, ...
	'FileName','N:\My Documents\Mathlab M-Files\Particle Packing\SaveDiscret.m', ...
	'MenuBar','none', ...
	'Name','Save Discretization', ...
	'NumberTitle','off', ...
	'PaperPosition',[18 180 576 432], ...
	'PaperUnits','points', ...
	'Position',[491.25 255 226.5 108], ...
	'Tag','Fig3', ...
	'ToolBar','none');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'BackgroundColor',[1 1 1], ...
	'HorizontalAlignment','left', ...
	'ListboxTop',0, ...
	'Position',[52.5 76.5 165 15], ...
	'String','C:\MATLABR11\work', ...
	'Style','edit', ...
	'Tag','EditText1');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'BackgroundColor',[0.8 0.8 0.8], ...
	'FontName','Arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[3.75 76.5 45 15], ...
	'String','Save in:', ...
	'Style','text', ...
	'Tag','StaticText1');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'Callback','SaveDiscretSave', ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[24.75 16.875 49.5 20.25], ...
	'String','Save', ...
	'Tag','Pushbutton1');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'Callback','close', ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[89.25 16.875 49.5 20.25], ...
	'String','Cancel', ...
	'Tag','Pushbutton2');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'Callback',mat1, ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[153.75 16.875 50.25 20.25], ...
	'String','Browse', ...
	'Tag','Pushbutton3');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'BackgroundColor',[0.8 0.8 0.8], ...
	'Callback',mat2, ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[30 49.5 63 15], ...
	'String','Split data', ...
	'Style','checkbox', ...
	'Tag','Checkbox1', ...
	'Value',1);
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'BackgroundColor',[1 1 1], ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[171 49.5 28.5 15], ...
	'String','10', ...
	'Style','edit', ...
	'Tag','EditText2');
h1 = uicontrol('Parent',h0, ...
	'Units','points', ...
	'BackgroundColor',[0.8 0.8 0.8], ...
	'FontName','arial', ...
	'FontSize',10, ...
	'ListboxTop',0, ...
	'Position',[99.75 49.5 71.25 15], ...
	'String','Nb. simulation:', ...
	'Style','text', ...
	'Tag','StaticText2');
if nargout > 0, fig = h0; end
