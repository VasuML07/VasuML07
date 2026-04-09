import { motion } from "framer-motion";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Github, Linkedin, ExternalLink } from "lucide-react";

export default function Portfolio() {
  return (
    <div className="bg-black text-white min-h-screen px-6 py-10">

      {/* HERO */}
      <section className="text-center space-y-6">
        <motion.h1
          initial={{ opacity: 0, y: -40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-5xl font-bold"
        >
          Vasu Avinash
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
          className="text-lg text-gray-400 max-w-xl mx-auto"
        >
          I build real-world Machine Learning systems — from raw data to deployed products.
        </motion.p>

        <div className="flex justify-center gap-4">
          <Button variant="outline"><Github className="mr-2"/>GitHub</Button>
          <Button variant="outline"><Linkedin className="mr-2"/>LinkedIn</Button>
          <Button><ExternalLink className="mr-2"/>Portfolio</Button>
        </div>
      </section>

      {/* SKILLS */}
      <section className="mt-20 grid md:grid-cols-3 gap-6">
        {[
          "Machine Learning Engineering",
          "Applied AI Systems",
          "Data Structures & Algorithms"
        ].map((skill, i) => (
          <motion.div
            key={i}
            initial={{ opacity: 0, y: 40 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.2 }}
          >
            <Card className="bg-zinc-900 border-none shadow-xl">
              <CardContent className="p-6 text-center">
                <p className="text-lg">{skill}</p>
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </section>

      {/* PROJECTS */}
      <section className="mt-20">
        <h2 className="text-3xl font-semibold mb-8">Projects</h2>

        <div className="grid md:grid-cols-2 gap-6">

          <motion.div whileHover={{ scale: 1.05 }}>
            <Card className="bg-zinc-900">
              <CardContent className="p-6">
                <h3 className="text-xl font-bold">Fake Job Detection</h3>
                <p className="text-gray-400 mt-2">
                  NLP pipeline using TF-IDF + Logistic Regression with 97.8% accuracy.
                </p>
              </CardContent>
            </Card>
          </motion.div>

          <motion.div whileHover={{ scale: 1.05 }}>
            <Card className="bg-zinc-900">
              <CardContent className="p-6">
                <h3 className="text-xl font-bold">Text-to-Image Generator</h3>
                <p className="text-gray-400 mt-2">
                  API-based generation system with prompt engineering and failure handling.
                </p>
              </CardContent>
            </Card>
          </motion.div>

        </div>
      </section>

      {/* SYSTEM THINKING */}
      <section className="mt-20">
        <h2 className="text-3xl font-semibold mb-6">How I Think</h2>

        <motion.ul
          initial="hidden"
          whileInView="visible"
          variants={{
            hidden: { opacity: 0 },
            visible: { opacity: 1 }
          }}
          className="space-y-3 text-gray-400"
        >
          <li>• Build systems, not just models</li>
          <li>• Simplicity scales better than complexity</li>
          <li>• Focus on failure cases first</li>
          <li>• Optimize for real-world impact</li>
        </motion.ul>
      </section>

      {/* STATS */}
      <section className="mt-20 grid md:grid-cols-3 gap-6 text-center">
        {[
          ["150+", "DSA Problems"],
          ["5+", "ML Projects"],
          ["Daily", "Consistency"]
        ].map(([num, label], i) => (
          <motion.div
            key={i}
            initial={{ scale: 0.8, opacity: 0 }}
            whileInView={{ scale: 1, opacity: 1 }}
            transition={{ delay: i * 0.2 }}
          >
            <h3 className="text-3xl font-bold">{num}</h3>
            <p className="text-gray-400">{label}</p>
          </motion.div>
        ))}
      </section>

      {/* FOOTER */}
      <footer className="mt-20 text-center text-gray-500">
        <p>Built with React + Tailwind + Framer Motion</p>
      </footer>

    </div>
  );
}
