const SDGs = [
    {
        id:"1",
        name:"abdul",
        indicators: [{id:"90", pet:"john", id:"87", pet: "cras"}]
    },
    {
        id:"2",
        name:"cardi",
        indicators: [{id:"74", pet:"bash", id:"47", pet: "niner"}]
    },
    {
        id:"3",
        name:"aisha",
        indicators: [{id:"51", pet:"april", id:"27", pet: "may"}]
    },
    {
        id:"4",
        name:"trip",
        indicators: [{id:"63", pet:"kiss", id:"12", pet: "tell"}]
    },
    {
        id:"5",
        name:"meek",
        indicators: [{id:"11", pet:"mill", id:"46", pet: "drip"}]
    },
]

//SDG Array up there

// Set empty array Variable
const available = []

// Push Selected SDGS id into available
{SDGs.map((sdgs)=>(
   available.push(sdgs.id)
 ))}

 // Filter Indicators
 available.pop()
 SDGs.filter((sdgs)=>{
   available.map((ava)=>{
        if(sdgs.id == ava){
            return(
                console.log(sdgs)
            )
    }
   })
 })

