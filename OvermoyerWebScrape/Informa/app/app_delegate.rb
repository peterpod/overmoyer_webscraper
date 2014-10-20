class AppDelegate
  def applicationDidFinishLaunching(notification)
    buildMenu
    buildWindow
  end

  def buildWindow
    @mainWindow = NSWindow.alloc.initWithContentRect([[1080, 480], [320, 240]],
      styleMask: NSTitledWindowMask|NSClosableWindowMask|NSMiniaturizableWindowMask|NSResizableWindowMask,
      backing: NSBackingStoreBuffered,
      defer: false)
    @mainWindow.title = NSBundle.mainBundle.infoDictionary['CFBundleName']
    @mainWindow.orderFrontRegardless
    
    @save_dest = ""
    
    create_dest_button
    create_run_button
  end
  
  def create_dest_button
    @dest_button = NSButton.alloc.initWithFrame(NSMakeRect(90, 180, 140, 24))
    @dest_button.title = "Save Report To..."
    @dest_button.setFont(NSFont.systemFontOfSize(13))
    @dest_button.action = :"save_to:" 
    @dest_button.target = self
    @dest_button.bezelStyle = NSRoundedBezelStyle 
    @mainWindow.contentView.addSubview(@dest_button)
  end
  
  def save_to(sender)
    save_browser = NSSavePanel.savePanel
    save_browser.canChooseFiles = false
    save_browser.canChooseDirectories = false
    save_browser.allowsMultipleSelection = false
    save_browser.nameFieldStringValue = "untitled.html"
      
    save_browser.beginSheetModalForWindow(@mainWindow, completionHandler:nil)
    if save_browser.runModal == NSFileHandlingPanelOKButton
      @save_dest = save_browser.filename
      # @save_dest = fix_str(save_browser.URLs.first.path)
      NSApp.endSheet(save_browser)
    end
  end
  
  def create_run_button
    @run_button = NSButton.alloc.initWithFrame(NSMakeRect(90, 100, 140, 24))
    @run_button.title = "Generate Report"
    @run_button.setFont(NSFont.systemFontOfSize(13))
    @run_button.action = :"run:"
    @run_button.target = self
    @run_button.bezelStyle = NSRoundedBezelStyle
    @mainWindow.contentView.addSubview(@run_button)
  end
  
  def run(sender)
    if @save_dest == ""
      print_warning
    else
      path = fix_str(NSBundle.mainBundle.bundleURL.path) + "/Contents/Resources/"
      `ruby #{path}format_tool.rb #{path} #{path}plaintext.txt #{@save_dest}`
    end
  end
  
  def print_warning
    title = "ERROR"
    msg = "Please enter a valid save destination."
    alert = NSAlert.alertWithMessageText(title, defaultButton: "Dismiss",
                                         alternateButton: nil, otherButton: nil,
                                         informativeTextWithFormat: msg)
    alert.alertStyle = 2
    alert.beginSheetModalForWindow(@mainWindow, modalDelegate:self,
                                   didEndSelector: nil, contextInfo:nil)
    NSApp.endSheet(alert)
  end
  
  def fix_str(string)
    if string.include?(" ")
      str_copy = string + ""
      str_copy.gsub!(/\s/, '\\ ')
    else
      string
    end
  end
  
end
