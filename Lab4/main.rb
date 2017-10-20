require_relative 'lab4/lab4'
require 'benchmark'
require 'plotly'

def multiply_ruby(a, b)
  puts a * b
end

def multiply_bind(a, b, l)
  l.multiply(a, b)
end

def multiply_native(a, b, l, n)
  l.time_multiply(a, b, n)
end

def hamming_ruby(a, b)
  (a^b).to_s(2).count("1")
end

def hamming_native(a, b, l, n)
  l.time_hamming(a, b, n)
end

def hamming_bind(a, b, l)
  l.hamming(a, b)
end


def main()
  l = Lab4.new
  
  ruby_results = Hash.new
  native_results = Hash.new
  bind_results = Hash.new
  for i in 1..100
    a = rand(1..2**31)
    b = rand(1..2**31)
    
    c = rand(1..2**15)
    d = rand(1..2**15)

    e = rand(1..2**7)
    f = rand(1..2**7)

    n = 1000

    #Sum of the numbers added together as an input size
    sum1 = a + b
    sum2 = c + d
    sum3 = e + f


    # Native Results
    native_results[sum1] = 1/multiply_native(a, b, l, n)
    native_results[sum2] = 1/multiply_native(c, d, l, n)
    native_results[sum3] = 1/multiply_native(e, f, l, n)


    # Ruby Results
    ruby_results[sum1] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_ruby(a, b)
      end
    }/n)
    
    ruby_results[sum2] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_ruby(c, d)
      end
    }/n)
    
    ruby_results[sum3] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_ruby(e, f)
      end
    }/n)

    #Binding Results
    bind_results[sum1] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_bind(a, b, l)
              end
    }/n)

    bind_results[sum2] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_bind(c, d, l)
      end
    }/n)

    bind_results[sum3] =1/( Benchmark.realtime{
      for i in 1..n
        multiply_bind(e, f, l)
      end
    }/n)

 
  end

  plotly = PlotLy.new('jvd5839', 'O1WM0mK7IMJXNOsyC1oR')
  args = {    
    filename: 'Multiply Times',
    fileopt: 'overwrite',
    style: { type: 'scatter' },
    layout: { 
    title: 'Iterations per Second for Multiplication' 
    }
  }
  
 data = [ 

    { x: ruby_results.keys,
      y: ruby_results.values,
      name: "Ruby Multiplication Implementation",
      marker: { color: 'rgb(26, 118, 255)'}
    },
    { x: native_results.keys,
      y: native_results.values,
      name: "Native Multiplication Implementation",
      marker: { color: 'rgb(55, 83, 240)' }
    },
    { x: bind_results.keys,
      y: bind_results.values,
      name: "Binding Multiplication Implementation",
      marker: { color: 'rgb(200, 144, 150)' }
    }
  ]

 plotly.plot(data, args) do |response|
   puts response['url']
  end
end

main()
