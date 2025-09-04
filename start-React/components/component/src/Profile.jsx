function Profile(props){
    return(
        <div>
            <p> name : {props.name} </p>
            <p> age : {props.age}  </p>
            <p>Bios: {props.Bios}</p>
        </div>
    )
}

export default Profile;