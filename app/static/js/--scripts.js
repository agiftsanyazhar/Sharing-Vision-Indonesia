async function fetchPosts() {
  let response = await fetch("http://127.0.0.1:5000/article/10/0");
  let result = await response.json();

  let postsContainer = document.getElementById("postsContainer");
  postsContainer.innerHTML = "";

  result.data.forEach((post) => {
    let postElement = document.createElement("div");
    postElement.classList.add("post");
    postElement.innerHTML = `
            <h3>${post.title}</h3>
            <p><strong>Category:</strong> ${post.category} | <strong>Status:</strong> ${post.status}</p>
            <p>${post.content}</p>
            <p><small>Created: ${post.created_date}</small></p>
            <div class="actions">
                <button onclick="editPost(${post.id}, '${post.title}', '${post.content}', '${post.category}', '${post.status}')">Edit</button>
                <button onclick="deletePost(${post.id})" style="background-color: red;">Delete</button>
            </div>
        `;
    postsContainer.appendChild(postElement);
  });
}

document
  .getElementById("postForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    let postId = document.getElementById("postId").value;
    let title = document.getElementById("title").value;
    let content = document.getElementById("content").value;
    let category = document.getElementById("category").value;
    let status = document.getElementById("status").value;

    let postData = { title, content, category, status };

    let url = "http://127.0.0.1:5000/article";
    let method = "POST";

    if (postId) {
      url = `http://127.0.0.1:5000/article/${postId}`;
    }

    let response = await fetch(url, {
      method: method,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(postData),
    });

    let result = await response.json();
    if (response.ok) {
      alert(result.message);
      location.reload();
    } else {
      alert("Error: " + result.message);
    }
  });

function editPost(id, title, content, category, status) {
  document.getElementById("postId").value = id;
  document.getElementById("title").value = title;
  document.getElementById("content").value = content;
  document.getElementById("category").value = category;
  document.getElementById("status").value = status;
  window.scrollTo(0, 0);
}

async function deletePost(id) {
  if (confirm("Are you sure you want to delete this post?")) {
    let response = await fetch(`http://127.0.0.1:5000/article/${id}`, {
      method: "DELETE",
    });
    let result = await response.json();
    alert(result.message);
    location.reload();
  }
}

fetchPosts();
