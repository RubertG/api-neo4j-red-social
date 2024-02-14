CREATE (ana:Usuario {id: "1", nombre: "Ana", email: "ana@ejemplo.com"})
CREATE (juan:Usuario {id: "2", nombre: "Juan", email: "juan@ejemplo.com"})
CREATE (maria:Usuario {id: "3", nombre: "María", email: "maria@ejemplo.com"})

// posts
CREATE (post1:Post {id: "1", contenido: "¡Hola a todos!", usuario_id: "1"})
CREATE (post2:Post {id: "2", contenido: "¿Alguien sabe cómo instalar Python?", usuario_id: "2"})
CREATE (post3:Post {id: "3", contenido: "Me encanta la pizza!", usuario_id: "3"})
CREATE (post4:Post {id: "4", contenido: "¿Qué opinan del nuevo álbum de Taylor Swift?", usuario_id: "2"})
CREATE (post5:Post {id: "5", contenido: "Estoy buscando un nuevo libro para leer, ¿alguna recomendación?", usuario_id: "2"})

// comentarios
CREATE (comentario1:Comentario {id: "1", contenido: "Hola Ana!", usuario_id: "2", post_id: "1"})
CREATE (comentario2:Comentario {id: "2", contenido: "Yo también estoy aprendiendo Python!", usuario_id: "3", post_id: "2"})
CREATE (comentario3:Comentario {id: "3", contenido: "La pizza con piña es la mejor!", usuario_id: "1", post_id: "3"})
CREATE (comentario4:Comentario {id: "4", contenido: "A mí me gusta más la de pepperoni", usuario_id: "2", post_id: "3"})
CREATE (comentario5:Comentario {id: "5", contenido: "Te recomiendo 'Cien años de soledad'", usuario_id: "3", post_id: "5"})

// Relaciones entre usuarios y posts 
CREATE (ana)-[:CREA]->(post1)
CREATE (juan)-[:CREA]->(post2)
CREATE (maria)-[:CREA]->(post3)
CREATE (juan)-[:CREA]->(post4)
CREATE (juan)-[:CREA]->(post5)

// usuario -> comentario 
CREATE (juan)-[:COMENTA]->(comentario1)
CREATE (maria)-[:COMENTA]->(comentario2)
CREATE (ana)-[:COMENTA]->(comentario3)
CREATE (juan)-[:COMENTA]->(comentario4)
CREATE (maria)-[:COMENTA]->(comentario5)

// Relaciones entre comentarios y posts
CREATE (comentario1)-[:EN_RESPUESTA_A]->(post1)
CREATE (comentario2)-[:EN_RESPUESTA_A]->(post2)
CREATE (comentario3)-[:EN_RESPUESTA_A]->(post3)
CREATE (comentario4)-[:EN_RESPUESTA_A]->(post3)
CREATE (comentario5)-[:EN_RESPUESTA_A]->(post5)
