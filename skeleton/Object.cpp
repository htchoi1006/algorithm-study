#include "Object.h"

// Face face;
// GLuint indices = face.num_indices;
// GLuint index_buffer = face.index_buffer;

void Object::init_buffer_objects()
{
  glGenBuffers(1, &position_buffer);
  glGenBuffers(1, &color_buffer);
  glGenBuffers(1, &index_buffer);
  // int j=0;
  

    // TODO

    std::vector<GLfloat> position;
    std::vector<GLfloat> colors;
    std::vector<GLuint> idx;

    for (unsigned int i = 0; i < pmesh_->mNumVertices; ++i)
    {
        aiVector3D vertex = pmesh_->mVertices[i];

        position.push_back(vertex.x);
        position.push_back(vertex.y );
        position.push_back(vertex.z);


        if (pmesh_->mColors[0] != NULL)
        {
            aiColor4D color = pmesh_->mColors[0][i];

            //glm::vec4 v=glm::vec4(color.r,color.g,color.b,color.a);
            colors.push_back(color.r);
            colors.push_back(color.g);
            colors.push_back(color.b);
            colors.push_back(color.a);

        }
    }
    for(unsigned int i=0; i<pmesh_->mNumFaces;i++){
      aiFace face=pmesh_->mFaces[i];
      for(unsigned int j=0; j<face.mNumIndices; j++){
        idx.push_back(face.mIndices[j]);
        num_indices ++;
      }
    }
      glBindBuffer(GL_ARRAY_BUFFER, position_buffer);
      glBufferData(GL_ARRAY_BUFFER,position.size()*sizeof(GLfloat)  ,&position[0], GL_STATIC_DRAW);


      glBindBuffer(GL_ARRAY_BUFFER, color_buffer);
      glBufferData(GL_ARRAY_BUFFER, colors.size()*sizeof(GLfloat),&colors[0], GL_STATIC_DRAW);



      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index_buffer);
      glBufferData(GL_ELEMENT_ARRAY_BUFFER, idx.size()*sizeof(GLuint),&idx[0], GL_STATIC_DRAW);


}

glm::mat4 Object::get_model_matrix() const{
    glm::mat4 mat_model = glm::mat4(1.0f);

    // TODO
    //mat_rot = glm::mat4_cast(rotate());
    mat_model = mat_model * glm::scale(glm::mat4(1.0f), vec_scale_);
    mat_model = mat_model * glm::mat4_cast(quat_rotate_);
    mat_model = mat_model * glm::translate(glm::mat4(1.0f),vec_translate_);

    return mat_model;
}

void Object::draw(int loc_a_position, int loc_a_color)
{
    // TODO
      glBindBuffer(GL_ARRAY_BUFFER, position_buffer);
      glEnableVertexAttribArray(loc_a_position);
      glVertexAttribPointer(loc_a_position, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);

      if (pmesh_->mColors[0] != NULL)
      {
        glBindBuffer(GL_ARRAY_BUFFER, color_buffer);
        glEnableVertexAttribArray(loc_a_color);
        glVertexAttribPointer(loc_a_color, 4, GL_FLOAT, GL_FALSE, 0, (void*)0);
      }

      glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, index_buffer);
      glDrawElements(GL_TRIANGLES, num_indices, GL_UNSIGNED_INT, (void*)0);

      glDisableVertexAttribArray(loc_a_position);
      glDisableVertexAttribArray(loc_a_color);
}

void Object::print_info()
{
    std::cout << "print mesh info" << std::endl;

    std::cout << "num vertices " << pmesh_->mNumVertices << std::endl;
    for (unsigned int i = 0; i < pmesh_->mNumVertices; ++i)
    {
        aiVector3D vertex = pmesh_->mVertices[i];
        std::cout << "  vertex  (" << vertex.x << ", " << vertex.y << ", " << vertex.z << ")" << std::endl;

        if (pmesh_->mColors[0] != NULL)
        {
            aiColor4D color = pmesh_->mColors[0][i];
            std::cout << "  color  (" << color.r << ", " << color.g << ", " << color.b << ", " << color.a << ")" << std::endl;
        }
    }
}