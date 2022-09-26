require 'open3'
require 'minitest/autorun'

Open3.popen3('python3 app.py') do |stdin, stdout, stderr, wait_thr|
  stdin.puts "1"
  stdin.puts "0"
  stdin.close                # we're done
  stdout_str = stdout.read   # read stdout to string. note that this will block until the command is done!
  stderr_str = stderr.read   # read stderr to string
  status = wait_thr.value    # will block until the command finishes; returns status that responds to .success? etc
  puts stdout_str
  puts stderr_str
  puts status
end
