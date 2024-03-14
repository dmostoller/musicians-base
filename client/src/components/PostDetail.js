import React, {useEffect, useState} from "react";
import {useParams, useNavigate} from "react-router-dom";
import {Link} from "react-router-dom";

function PostDetail({}){
    const [post, setPost] = useState({})
    const {id} = useParams();
    const navigate = useNavigate();

    useEffect(() => {
        fetch(`/posts/${id}`)
        .then((res) => res.json())
        .then((post) => setPost(post))
    }, [id]);

    const handleDeletePost = (e) => {
        if (window.confirm("Are you sure you want to delete this post?")) {
        fetch(`/posts/${id}`, {
            method: "DELETE"
            })
            .then(() => {
                // deletePost(post)
                navigate('/') 
            })
        }
    }    
    return (
    <div className="ui container" style={{marginTop:"45px"}}>
        <div className="ui relaxed inverted divided items">
            <div className="item" >
                <div className="ui huge image" style={{marginTop:"25px"}}>
                    <img src={post.image_url} alt={post.title}></img>
                </div>
                <div className="content" style={{marginTop:"75px"}}>
                    <div className="header">
                        {post.title}
                    </div>
                    <div className="meta">
                        <span className="category">{post.date_added}</span>
                    </div>
                    <div className="description">
                        <p>{post.content}</p>
                    </div>
                    <div style={{padding: "10px"}}> 
                        <Link to="/" className="circular ui icon inverted grey button"><i className="undo icon"></i></Link>
                        {/* { user && isAdmin ? ( */}
                                        {/* <> */}
                                            <Link to={`/posts/${id}/edit`} className="circular ui icon inverted grey button">
                                                <i className="edit icon" style={{visibility: "visible"}}></i>
                                            </Link>
                                            <button className="circular ui icon inverted grey button" onClick={handleDeletePost}>
                                                <i class="trash icon" style={{visibility: "visible"}}></i>
                                            </button>

                                        {/* </>
                                        )
                                        : <></>    
                                    } */}
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    );
}

export default PostDetail