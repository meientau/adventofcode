(defun move-to-start ()
  (goto-char (point-min))
  (let ((case-fold-search nil)) (search-forward "S"))
  (goto-char (match-beginning 0)))

(defun can-go-right ()
  (and
   (< (point) (point-max))
 ))

(defun can-go-left ()
  (and
   (> (point) (point-min))
   (eq ?w (save-excursion (left-char) (char-after)))))

(defun can-go-down ()
  (and
   (< (point) (point-max))
   (eq ?w (save-excursion (next-line) (debug) (char-after)))))

(defun can-go-up ()
  (and
   (> (point) (point-min))
   (eq ?w (save-excursion (previous-line) (char-after)))))

(defvar possible-steps
  '(
    (can-go-right right-char ?>)
    (can-go-left left-char ?<)
    (can-go-up previous-line ?^)
    (can-go-down next-line ?_)
    )
  )

(defun step-predicate (def) (car def))
(defun step-action (def) (car (cdr def)))
(defun step-symbol (def) (car (cdr (cdr def))))

(defun take-a-step (def)
  (let ((beg (point))
        (end))
    (save-excursion
      (funcall (step-action def))
      (setq end (point))
      (if (and (neq beg end)
               (eq ?w (char-after end)))
          (progn
            (goto-char (beg))
            (delete-char 1)
            (insert-char (step-symbol def))
            (sit-for 0.1)
            (take-all-next-steps)
            (undo))))))

(defun take-all-next-steps ()
  (mapcar 'take-a-step possible-steps))

(defun find-best-signal ()
  (interactive)
  (write-file ".temp")
  (move-to-start)
  (take-all-next-steps))
