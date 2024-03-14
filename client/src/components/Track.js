import React from "react"
// import song from "../audio/Superluminal - Multi Dimensional Perception 152 A TRK M 16 Bit.wav"

export default function Track({title, artist_names, bpm, audio}) {
    return (
        <div className="item" style={{padding: "10px"}}>
            <div className="content">
                <div><h5>{title}</h5></div>
                <div className="meta">
                    <span>{artist_names}</span>
                    <span>{bpm} bpm</span>
                </div>
                <div className="description">
                    <div>AUDIO FILE GOES HERE{audio}</div>
                </div>
            </div>


        </div>
    )

}