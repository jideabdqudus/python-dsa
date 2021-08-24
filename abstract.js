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



import React from 'react'
import {Divider, Checkbox, Spin} from "antd"

interface Props {
  sdgsAndIndicators: any
  onClickSdg: (e: any)=> void
  indicatorsUnderSdgs: [] | undefined
  onSelectIndicator: (checkedValues: any)=> void
  loading?: boolean,
  sdgId: any
  selectedSdgs: any,
  getIndicators: ()=> void
}
export const SdgGroup:React.FC<Props> = ({sdgsAndIndicators, onClickSdg, onSelectIndicator, loading, sdgId, selectedSdgs, getIndicators}) => {
  // const getIndicators = ()=>{

  // }
  return (
    <div className="sdg-group">
     <Divider orientation="right">Select SDGs for the programme</Divider>
      { loading?
        <div className="sdg-loader">
          <Spin tip="Loading Development Goals..." />
        </div>
        :
        <ul>
          {sdgsAndIndicators && sdgsAndIndicators.map((sdgs: any)=>(
            <li key={sdgs.id}>
              <input type="checkbox" value={sdgs.id} name={sdgs.name} id={sdgs.id} onClick={onClickSdg} />
              <label htmlFor={sdgs.id}><img src={sdgs.image} alt="SDGs" /></label>
            </li>
          ))}
        </ul>
      }

      {getIndicators()}

      { selectedSdgs && selectedSdgs?.length > 0 ?
        <Divider orientation="right">Select SDG Indicators</Divider> : null }

      { selectedSdgs && selectedSdgs?.length > 0 ? selectedSdgs.map((sdg: any)=>{
        return (
          sdg.indicators.map((indicator: any, i: number)=>{
            return (
            <div className="indicator-style">
              {i === 0 && <h1>{sdg.name}</h1>}
                <Checkbox.Group className="indicator-style__checks" onChange={onSelectIndicator}>
                      <Checkbox value={indicator.id}>{indicator.description}</Checkbox>
                </Checkbox.Group>
            </div>
            )}))
          })
          :
          null
      }
      </div>

  )
}











import React, {useState, useEffect} from 'react'
import {Divider, Checkbox} from "antd"

interface Props {
  sdgsAndIndicators: any
  onClickSdg: (e: any)=> void
  indicatorsUnderSdgs: [] | undefined
  onSelectIndicator: (checkedValues: any)=> void
  loading?: boolean,
  sdgId: any
  selectedSdgs: any,
  getIndicators: ()=> void
}
export const SdgGroup:React.FC<Props> = ({sdgsAndIndicators, onClickSdg, indicatorsUnderSdgs, onSelectIndicator, loading}) => {
  const [available, setAvailable] = useState<any>([])
  let arr: any = []
  const onClickHere = (e: any)=>{
    // console.log(random)
    setAvailable([...available, e.target.value])
    // dispatch(getIndicatorsUnderSdgs(e.target.value))
  }

  const setIndicators = ()=>{
    sdgsAndIndicators.filter((sdgs : any)=>{
      available.map((ava: any)=>{
        if(sdgs.id === ava){
            arr.push(sdgs)
        }
        return null
      })
      return null
    })
  }

  return (
    <div className="sdg-group">
      {sdgsAndIndicators && <Divider orientation="right">Select SDGs for the programme</Divider>}
           {/* {loading?  <div className="sdg-loader"> <Spin tip="Loading Development Goals..." /> </div> :
            <ul>
              {sdgsAndIndicators && sdgsAndIndicators.map((sdgs: any)=>(
                <li key={sdgs.id}>
                  <input type="checkbox" value={sdgs.id} name={sdgs.name} id={sdgs.id} onClick={onClickSdg} />
                  <label htmlFor={sdgs.id}><img src={sdgs.image} alt="SDGs" /></label>
                </li>
              ))}
            </ul> } */}
            <ul>
              {sdgsAndIndicators && sdgsAndIndicators.map((sdgs: any)=>(
                <li key={sdgs.id}>
                  <input type="checkbox" value={sdgs.id} name={sdgs.name} id={sdgs.id} onClick={onClickHere} />
                  <label htmlFor={sdgs.id}><img src={sdgs.image} alt="SDGs" /></label>
                </li>
              ))}
            </ul>
            {setIndicators()}

            {arr && arr?.length > 0 ?  <Divider orientation="right">Select SDG Indicators</Divider> : null }

              { arr && arr?.length > 0 ? arr.map((ar: any)=>{
                return (
                  ar.indicators.map((indi: any, i: number)=>{
                  return (
                    <div className="indicator-style">
                      {i === 0 && <h1>{ar.name}</h1>}
                    <Checkbox.Group className="indicator-style__checks" onChange={onSelectIndicator} key={indi.id}>
                          <Checkbox value={indi.id}>{indi.description}</Checkbox>
                    </Checkbox.Group>
                    </div>
                  )})
                )
               }): null}

      </div>

  )
}





