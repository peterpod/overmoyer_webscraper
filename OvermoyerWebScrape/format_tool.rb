# format_tool.rb
#
# The Informants: Achal Channarasappa, Duncan McIsaac,
# Graham Schilling, Matt Nielsen, Peter Pod

require "erb"

class FormatTool
  
  def initialize(source, destination)
    @source = source
    @destination = destination
    @content = []
  end
  
  def run
    parse_info
    generate_text_file
  end
  
  def parse_info
    competitor = Hash.new
    current = nil
    
    File.foreach(@source) do |row|
      
      if row =~ /^End/
        @content << competitor
        competitor = Hash.new
      elsif row =~ /^Name/
        competitor[:name] = get_name(row)
        current = :name
      elsif row =~ /^Stock/
        competitor[:stock] = get_stock(row)
        current = :stock
      elsif row =~ /^Mission/
        competitor[:mission] = get_mission(row)
        current = :mission
      elsif row =~ /^News/
        competitor[:news] = get_news(row)
        current = :news
      elsif row =~ /^Products/
        competitor[:products] = get_products(row)
        current = :products
      elsif row =~ /^Misc/
        competitor[:misc] = get_misc(row)
        current = :misc
      elsif row == "\n"
        competitor[current] << "<br /><br />"
      else
        competitor[current] << row
      end
      
    end
    
    @content << competitor
    
  end
  
  def generate_text_file
    File.open(@destination, "a") do |dest|
      Writer.new(@content, dest).save
    end
  end
  
  def get_name(row)
    row[5..-1]
  end
  
  def get_stock(row)
    row[6..-1]
  end
  
  def get_mission(row)
    row[8..-1]
  end
  
  def get_news(row)
    row[5..-1]
  end
  
  def get_products(row)
    row[9..-1]
  end
  
  def get_misc(row)
    row[5..-1]
  end
  
end

class Writer
  
  def initialize(content, destination)
    @content = content
    @destination = destination
    @template = File.open("template.html.erb", "r").read
  end

  def save
    render = ERB.new(@template, nil, ">").result(binding)
    @destination.write(render)
  end
  
end

if __FILE__ == $0
  source, destination = ARGV
  
  formatter = FormatTool.new(source, destination)
  formatter.run
end
