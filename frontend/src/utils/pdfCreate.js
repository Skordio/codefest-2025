import { generate } from "@pdfme/generator";

// @ts-nocheck

// Define the JSON Data
const exampleStudyGuideJsonData = {
  study_guide: [
    {
      main_point: "Introduction to PDF Generation",
      subpoints: ["Uses of PDFs", "Common Libraries", "Benefits of Automation"],
      explanation: "Generating PDFs programmatically is useful for reports, invoices, and structured documents."
    },
    {
      main_point: "pdfme Library Overview",
      subpoints: ["Template-based PDF creation", "WYSIWYG Editor", "Customizable Outputs"],
      explanation: "pdfme allows you to define PDF structures using JSON, making it highly flexible."
    }
  ]
};

const exampleFlashCardJsonData = {
  flashcards: [
    {
        "explanation": "The Constitution of the United States was created to establish a form of government that protects rights and promotes a perfect union.",
        "term/concept": "Purpose of the Constitution"
    },
    {
        "explanation": "The Declaration of Independence is viewed as a radical document focused on universal rights, while the Constitution is seen as a conservative document focused on government structure and protection of those rights.",
        "term/concept": "Declaration of Independence vs Constitution"
    },
  ]
}

const exampleQuizJsonData = {
  quiz: [
    {
        "answer": "True",
        "choices": [
            "True",
            "False"
        ],
        "question": "The course mentioned is about the Constitution of the United States."
    },
    {
        "answer": "b",
        "choices": [
            "a) True",
            "b) False",
            "c) Only in 1776",
            "d) Only in 1787"
        ],
        "question": "The Declaration of Independence and the Constitution serve the same purpose."
    }
]
}




function createStudyGuidePDF(jsonData) {
  // Define a PDF template structure
  const template = {
    basePdf: null, // No background PDF needed
    schemas: [
      {
        main_point: { type: "text", position: { x: 50, y: 40 }, width: 500, height: 20, fontSize: 16, bold: true },
        subpoints: { type: "text", position: { x: 50, y: 70 }, width: 500, height: 50, fontSize: 12 },
        explanation: { type: "text", position: { x: 50, y: 120 }, width: 500, height: 50, fontSize: 12 }
      }
    ]
  };

  // Convert JSON Data to a pdfme-friendly format
  const inputs = jsonData.study_guide.map((section, index) => ({
    main_point: section.main_point,
    subpoints: section.subpoints.map((subpoint, i) => `${i + 1}. ${subpoint}`).join("\n"),
    explanation: section.explanation
  }));

  // Generate the PDF
  (async () => {
    const pdfBuffer = await generate({ template, inputs });

    // Create file object
    return new Blob([pdfBuffer], { type: "application/pdf" });
  })();
}

function createFlashCardPDF(jsonData) {
  // Define a PDF template structure
  const template = {
    basePdf: null, // No background PDF needed
    schemas: [
      {
        "term/concept": { type: "text", position: { x: 50, y: 40 }, width: 500, height: 20, fontSize: 16, bold: true },
        "explanation": { type: "text", position: { x: 50, y: 70 }, width: 500, height: 50, fontSize: 12 }
      }
    ]
  };

  // Convert JSON Data to a pdfme-friendly format
  const inputs = jsonData.flashcards.map((flashcard, index) => ({
    "term/concept": flashcard["term/concept"],
    "explanation": flashcard["explanation"]
  }));

  // Generate the PDF
  (async () => {
    const pdfBuffer = await generate({ template, inputs });

    // Create file object
    return new Blob([pdfBuffer], { type: "application/pdf" });
  })();
}

function createQuizPDF(jsonData) {
  // Define a PDF template structure
  const template = {
    basePdf: null, // No background PDF needed
    schemas: [
      {
        question: { type: "text", position: { x: 50, y: 40 }, width: 500, height: 20, fontSize: 16, bold: true },
        choices: { type: "text", position: { x: 50, y: 70 }, width: 500, height: 50, fontSize: 12 }
      }
    ]
  };

  // Convert JSON Data to a pdfme-friendly format
  const inputs = jsonData.quiz.map((quiz, index) => ({
    question: quiz.question,
    choices: quiz.choices.map((choice, i) => `${String.fromCharCode(97 + i)}) ${choice}`).join("\n")
  }));

  // Generate the PDF
  (async () => {
    const pdfBuffer = await generate({ template, inputs });

    // Create file object
    return new Blob([pdfBuffer], { type: "application/pdf" });
  })();
}

export { createStudyGuidePDF, createFlashCardPDF, createQuizPDF };