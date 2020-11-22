(n=>{

    fizz = 3
    buzz = 5
    list = []
    
    for(let i=1; i<=n; i++){
        
        switch(i%fizz+i%buzz){
        
            case 0:
                list.push('FizzBuzz')
                break;

            default:
                switch(i%fizz){
                    
                    case 0:
                        list.push('Fizz')
                        break;

                    default:
                        switch(i%buzz){
                    
                            case 0:
                                list.push('Buzz')
                                break;

                            default:

                                list.push(i)
                        }
                }
        }
    }

    return list

})(100)