class IRB::Context
   attr_accessor :max_output_size

   alias initialize_before_max_output_size initialize
   def initialize(*args)
     initialize_before_max_output_size(*args)
     @max_output_size = IRB.conf[:MAX_OUTPUT_SIZE] || 300
   end
end

class IRB::Irb
   def output_value
     text =
       if @context.inspect?
         sprintf @context.return_format, @context.last_value.inspect
       else
         sprintf @context.return_format, @context.last_value
       end
     max = @context.max_output_size
     if text.size < max
       puts text
     else
       puts text[0..max-1] + "..." + text[-2..-1]
     end
   end
end

irbrc_rails_path = File.expand_path('~/.irbrc_rails')
if (defined? Rails) && File.exist?(irbrc_rails_path)
  begin
    load irbrc_rails_path
  rescue Exception
    warn "Unable to load rails rc file at \"#{irbrc_rails_path}\" (#{$!.message})"
  end
end

