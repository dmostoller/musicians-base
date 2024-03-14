import React, {useState, useEffect} from "react";
import Post from "./Post";
import { Link } from "react-router-dom"

function PostsList ({}) {
    const [posts, setPosts] = useState([])

    useEffect(() => {
      fetch(`/posts`)
      .then((res) => res.json())
      .then((posts) => {setPosts(posts)})
    }, []);

    const sortedPosts = posts.sort((a, b) => (a.date_added) > (b.date_added) ? -1 : 1)

    const blog = sortedPosts.map((post) => {
        return <Post 
        key={post.id}
        id={post.id} 
        title={post.title}
        content={post.content}
        image_url={post.image_url}
        date_added={post.date_added}
        isAdmin='true'
        />
    })

    return (
        <>
        {/* {(user && isAdmin) ?   */}

            {/* : <div></div>
        } */}
            <div className="ui grid container centered">{blog}

            </div>
            <div className="ui grid container centered">
                <Link to={`/posts/new`} style={{margin: "10px"}} className="ui icon secondary button"><i className="plus icon"></i>  New Post</Link>
            </div>
        </>
    )
}

export default PostsList