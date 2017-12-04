// Synopsis des classes

// Classe Variable
class Variable {
	domain_; // Ici on met le domaine : il faut déterminer le type
	delta_; // Ici on met le delta : il faut déterminer le type
	Propagation* p_;// Définir ici un pointeur vers la fn de propagation : quand une var est modifiee on l'ajoute dans la queue si elle n'y est pas deja
public:
	bool is_in_domain(int a){
		// retourne vraie si a est dans le domaine et faux sinon
	}
	bool remove_value(int a){ // Cette fonction retourne faux si on supprime le dernier element du domaine
		if (is_in_domain(a){
			// Ecrire le code : on supprime la valeur a. Pour simplifier on peut considerer que les valeurs vont de 0 à d
			add_to_delta(a); // on ajoute a dans le delta de la variable
			p_->add_to_queue(this);
		}
		return true;
	}
	bool is_delta_empty(){
		// retourne vraie si le delta est vide et faux sinon
	}
	void reset_delta(){
		// cette fonction remet le delta à 0
	}
};

// Classe Propagation
class Propagation {
	queue_; // Il faut determiner son type : elle contient les variable qui ont un delta non nul.
	// Mettre ici le graphe des contraintes : ie pour chaque variable l'ensemble des contraintes impliquant la variable
public:
	void add_to_queue(Variable* x){
		// Cette fonction ajoute x dans la queue si x n'est pas déja dans la queue (on peut mettre un marqueuer dans Variable ou bien fait un tableau de marqueur
	}
	pick_in_queue(){ 
		// Il faut déterminer son type de retour
		// cette fonction prend une var dans la queue et la supprime de la queue
		return XXX; // A définir
	}
	run(){
		// tant que queue_ n'est pas vide
			// prendre x dans queue_ avec pick in queue
			// pour chaque contrainte c impliquant x
				// bool ret=c->filter_from(x);
				// if (!ret) // on arrete l'algo: un domaine est vide
			// fin pour
			// x->reset_delta();
		// fn tant que
	}
};

// Classe Contrainte:dans cette version il y a une seule classe par contrainte. Cette classe sera donc présente dans la liste des contraintes de x
// et dans la liste des contraintes de y
class Contrainte { // on ne fait que du binaire
	x_; // premiere var
	y_; // seconde var
	table_; // faire une structure de table
public :
	// faire le ctor (constructeur) qui prend la table
	virtual bool filter_from(Variable *x){ // Cette fonction retourne faux si on  a vider un domaine !
		// L'idee générale est :
		if (x==&x_){ // on filtre a partir du domaine de x_, donc on doit filter y_
		} else {// on filtre a partir du domaine de y_, donc on doit filter x_
		}
	}
};

// Si on veut faire AC-3 alors on crée une classe
class AC3ContrainteDeTable : public Contrainte {
	bool filter_from(Variable* x){
		// on implémente le filtrage AC3
	}
};

// On emploiera toujours cette classe pour les table si on veut faire AC3

// Si on veut faire AC4 on définir
class AC4ContrainteDeTable : public Contrainte {
	bool filter_from(Variable* x){
		// on implémente le filtrage AC4
	}
};

// Et ainsi de suite pour AC6 et AC-2001

// TODO : il faut faire le graphe des contraintes, les constructeurs et destructeurs (si vous faites en C++) des classes
// Il faut aussi completer les classes et definir les filtrages
