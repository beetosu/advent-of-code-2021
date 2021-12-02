def single_inc
    prior = -1
    amount = 0
    numbers = File.read("input").split 
    for number in numbers do 
        if number.to_i > prior
            amount = amount + 1
        end
        prior = number.to_i 
    end
    puts amount - 1
end

def group_inc
    prior = -1
    amount = 0
    numbers = File.read("input").split 
    for number in 0..numbers.length() do 
        sum = numbers[number].to_i
        if number < numbers.length()-1
            sum = sum + numbers[number+1].to_i
        end
        if number < numbers.length()-2
            sum = sum + numbers[number+2].to_i
        end
        if sum > prior
            amount = amount + 1
        end
        prior = sum
    end
    puts amount - 1
end

group_inc