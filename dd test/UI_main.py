# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,380 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )
		
		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( sbSizer2.GetStaticBox(), wx.ID_ANY, u"性能测试" ), wx.VERTICAL )
		
		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )
		
		gSizer9 = wx.GridSizer( 0, 2, 0, 0 )
		
		sbSizer8 = wx.StaticBoxSizer( wx.StaticBox( sbSizer4.GetStaticBox(), wx.ID_ANY, u"测试选项" ), wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText4 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"需要测试请勾上", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_staticText5 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输入节点，如/dev/sda1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		fgSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( sbSizer8.GetStaticBox(), wx.ID_ANY, u"输入次数，默认3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		self.m_checkBox23 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"EMMC", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox23.SetValue(True) 
		fgSizer1.Add( self.m_checkBox23, 0, wx.ALL, 5 )
		
		self.m_textCtrl22 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"默认不用填", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl22, 0, wx.ALL, 5 )
		
		self.m_textCtrl32 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl32.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl32, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox24 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"USB2.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox24.SetValue(True) 
		fgSizer1.Add( self.m_checkBox24, 0, wx.ALL, 5 )
		
		self.m_textCtrl23 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"/dev/sda1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl23, 0, wx.ALL, 5 )
		
		self.m_textCtrl33 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl33.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl33, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox25 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"USB3.0", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox25, 0, wx.ALL, 5 )
		
		self.m_textCtrl24 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"/dev/sda1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl24, 0, wx.ALL, 5 )
		
		self.m_textCtrl34 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size( 3,-1 ), 0 )
		self.m_textCtrl34.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl34, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox26 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"SATA-SSD", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox26, 0, wx.ALL, 5 )
		
		self.m_textCtrl25 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"/dev/sda1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl25, 0, wx.ALL, 5 )
		
		self.m_textCtrl35 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl35.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl35, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox27 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"PCIE-SSD", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox27, 0, wx.ALL, 5 )
		
		self.m_textCtrl26 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"/dev/nvme0n1p1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl26, 0, wx.ALL, 5 )
		
		self.m_textCtrl36 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl36.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl36, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		self.m_checkBox28 = wx.CheckBox( sbSizer8.GetStaticBox(), wx.ID_ANY, u"Sdcard", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_checkBox28, 0, wx.ALL, 5 )
		
		self.m_textCtrl37 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"/dev/mmcblk0p1", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_textCtrl37, 0, wx.ALL, 5 )
		
		self.m_textCtrl38 = wx.TextCtrl( sbSizer8.GetStaticBox(), wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl38.SetMinSize( wx.Size( 50,-1 ) )
		
		fgSizer1.Add( self.m_textCtrl38, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer8.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		
		gSizer9.Add( sbSizer8, 1, 0, 5 )
		
		
		gSizer6.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		self.m_button2 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"设置性能模式", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer6.Add( self.m_button2, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		sbSizer4.Add( gSizer6, 1, wx.EXPAND, 5 )
		
		self.m_button11 = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"开始测试", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer4.Add( self.m_button11, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		
		sbSizer2.Add( sbSizer4, 1, wx.EXPAND, 5 )
		
		
		bSizer4.Add( sbSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_checkBox24.Bind( wx.EVT_CHECKBOX, self.ChoseBox_Event )
		self.m_checkBox25.Bind( wx.EVT_CHECKBOX, self.ChoseBox_Event )
		self.m_checkBox26.Bind( wx.EVT_CHECKBOX, self.ChoseBox_Event )
		self.m_checkBox27.Bind( wx.EVT_CHECKBOX, self.ChoseBox_Event )
		self.m_button2.Bind( wx.EVT_BUTTON, self.SetPerformance )
		self.m_button11.Bind( wx.EVT_BUTTON, self.Start_Test )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def ChoseBox_Event( self, event ):
		event.Skip()

	def SetPerformance( self, event ):
		event.Skip()
	
	def Start_Test( self, event ):
		event.Skip()
	