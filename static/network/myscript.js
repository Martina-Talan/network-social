
document.addEventListener('DOMContentLoaded', function () {
    // Like/Unlike
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }

    function toggleLike(postID, action) {
        fetch(`/like_post/${postID}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),
            },
            body: JSON.stringify({ action: action }),
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const likeCountElement = document.querySelector(`.likes[data-post-id="${postID}"]`);
                if (likeCountElement) {
                    likeCountElement.textContent = data.likes + ' Like(s)';
                }

                const likeButton = document.querySelector(`.like-button[data-post-id="${postID}"]`);
                const unlikeButton = document.querySelector(`.unlike-button[data-post-id="${postID}"]`);

                if (action === 'like') {
                    likeButton.style.display = 'none';
                    unlikeButton.style.display = 'inline-block';
                } else {
                    unlikeButton.style.display = 'none';
                    likeButton.style.display = 'inline-block';
                }
            } else {
                console.error(data.message);
            }
        });
    }

    document.addEventListener('click', function (event) {
        if (event.target.classList.contains('like-button') || event.target.classList.contains('unlike-button')) {
            const postID = event.target.getAttribute('data-post-id');
            const action = event.target.getAttribute('data-action');
            toggleLike(postID, action);
        }
    });


    // Edit post
    const editButtons = document.querySelectorAll('.edit-button');
    
    editButtons.forEach((editButton) => {
        editButton.addEventListener('click', function() {
            const parentDiv = this.parentElement;
            const editForm = parentDiv.querySelector('.edit-form');
            const editTextarea = editForm.querySelector('.edit-textarea');
    
            const postContent = parentDiv.querySelector('.post-content').innerHTML;
            editForm.style.display = 'block';
            editTextarea.value = postContent; 
        });
    });
    
    // Save edited post
    const saveButtons = document.querySelectorAll('.save-button');
    
    saveButtons.forEach((saveButton) => {
        saveButton.addEventListener('click', function(event) {
            event.preventDefault();
            const parentForm = this.parentElement;
            const editTextarea = parentForm.querySelector('.edit-textarea');
            
        
            const postID = this.getAttribute('data-post-id');
            const newPostContent = editTextarea.value;
            
            fetch(`/edit_post/${postID}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'),
                },
                body: JSON.stringify({ post_content: newPostContent }),
            })
            .then(response => response.json())
            .then(data => {
                const postContentElement = document.querySelector(`[data-post-id="${postID}"] .post-content`);
                postContentElement.innerHTML = newPostContent;
                parentForm.style.display = 'none';
            });
        });
    });
})    