<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0689.txt",
      "sha256": "38a78aaea83fbfb7289c9c760b1530b5613f9b087a646ac8a9dd1b7321f544f3",
      "bytes": 14518
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "143e8fbe00758a2f14ae31c4682eecb3039e96647fed729fbcb15431f38091df",
      "bytes": 2370
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "3bd36033a8e83ea76cb8345710c858f69987095efab9064f44135007a7214e6b",
      "bytes": 204372
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "146c3dd48a33c63824125d98006b30b47402ce881126976f48694c4514762d80",
      "bytes": 553
    },
    {
      "path": "characters/Heugung.md",
      "sha256": "e88b97ec7ba9c80070fabbd014a4dfb117d9da9f09218d986b20c1fe92ceb938",
      "bytes": 784
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "94c56c360768caff0412cf7bd2b686e7073262871c7ca0db0b9c03968c1fe167",
      "bytes": 1883
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "4b8813c7698c987ca98098f49a2794d52b64808b8ab069b0392c3676b3e66927",
      "bytes": 622
    },
    {
      "path": "characters/Muyaho.md",
      "sha256": "d57bf7ff00695d9691666c23edf4d2c5688c93a6ff0c94e1a03b368f0c48d4ba",
      "bytes": 613
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "38325d2a1a6e9e16532457f9fef277391aa269e24c4f61885c55673433ff47f8",
      "bytes": 554
    },
    {
      "path": "characters/Yayul Mok.md",
      "sha256": "c660c2bd51a006b8e936f21bec3cdd3cfc76167e74de3bf51aea811d864627b8",
      "bytes": 864
    },
    {
      "path": "characters/Yohi.md",
      "sha256": "55d555aa6dcf51207dfbb507f81acdf31f72358322e1ce3d736990031f546144",
      "bytes": 678
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a720dac79e4255aa153cf01d265a94fd19f8bcf18364b96fdcb4eb63ca056f7f",
      "bytes": 212512
    }
  ],
  "estimated_tokens": 11914
}
-->

# Durable State Update — Chapter 689

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 689. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 689. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 689,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 689,
    "continuity_sources": [689],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Baeksang now exercises full Palace Lord authority over the Nanman Beast Palace and is consolidating power through total mobilization and the removal of disloyal tribes.",
    "The Miao Head Elder rejected Baeksang's demand that the Miao people betray Yayul Cheok and was imprisoned with the Miao leadership.",
    "The Southern Heaven Demon Empress considers Yayul Cheok and Jin Taekyung no longer important to the grand plan and has ordered the Inner and Outer Palaces fortified.",
    "The grand plan is scheduled to begin and end within three days.",
    "Jin Taekyung broke the trap at Ailao Mountain after defeating two Supreme Peak masters, one of whom was the Black Hand Fist Demon.",
    "Heugung is secretly the Beast Miao King and can transform between their identities through the Bone-Shrinking Technique at Great Completion.",
    "Heugung has taken control of the unconscious Jin Taekyung after Jin defeated the two Supreme Peak masters, while the exhausted White Tiger remains alive.",
    "Heugung has incapacitated Yohi with a sinister substance or energy after revealing his identity and withholding the genuine antidote.",
    "Heugung plans to bring Jin and Yohi to the Inner Palace and fabricate a story that Jin and the Murim Alliance plotted to invade and destroy Nanman.",
    "Heugung threatens to slaughter more than five thousand Yao people at Boshan to force Yohi's compliance.",
    "A blade-like wind attacked Heugung as he tried to lift Jin, and the outcome remains unresolved."
  ],
  "continuity_sources": [
    688,
    687
  ],
  "open_questions": [
    "What created the blade-like wind, and did the attack injure or stop Heugung?",
    "Will Yohi and Jin remain under Heugung's control after the attack?",
    "Will Yohi submit to Heugung's fabricated account to save the Yao people at Boshan?",
    "Can Heugung still carry out the plan to mobilize Nanman against the Central Plains?",
    "What will begin and end when the Southern Heaven Demon Empress's three-day deadline arrives?"
  ],
  "safe_through": 688,
  "temporary_decisions": [
    "Render 궁주 as Palace Lord.",
    "Render 대장로 as Head Elder.",
    "Render 백천대 as Baekcheon Unit.",
    "Render 기호지세 as \"Once you are riding a tiger, you cannot get off.\"",
    "Render 대마 as major piece."
  ],
  "version": 1
}
```

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 영약     | **elixir**                                       |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 제자     | **Disciple**                                 |
| 상태               | **Status**                     |
| 귀가      | **your family**                                                 |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 흑웅 | **Heugung** | Great chieftain of the Yi people; his name literally means Black Bear. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 야율목 | **Yayul Mok** | Young Palace Lord of the Nanman Beast Palace. |
| 요희 | **Yohi** | Female great chieftain of the Yao people. |
| 평화 | **Peace Guild** | Guild name. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 연검 | **flexible sword** | Ju Hwaran's weapon. |
| 단환 | **pill** | A martial elixir in pill form; Mungyeong gives Taekyung a custom-made one. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 철옹성 | **impregnable fortress** | Metaphor for Ares Guild's entrenched defenses. |
| 요족 | **Yao people** | One of Nanman's four great tribes, led by Yohi. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 서리 | **seori** | Colloquial term for stealing crops or produce from a field. |
| 흑호 | **Black Tiger** | A colossal black tiger that appears at the Ailao Mountain massacre site. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 야율 | **Yayul** | Name used in Taekyung's colloquial address to the Beast Miao King. |
| 대족장 | **Great Chieftain** | Title used for the senior Nanman leader who supposedly ordered the inspection. |
| 소궁주 | **Young Palace Lord** | Title used for Yayul Mok as heir of the Nanman Beast Palace. |
| 요서부 | **Western Yao Estate** | Estate inherited by Yohi when she became a Great Chieftain. |
| 궁주 | **Palace Lord** | Title Yohi uses after realizing that Heugung is the Beast Miao King. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 진태경 | 청년 | celebrated Hunter to younger fellow Hunter | young man | casual, teasing, and profane | Jin addresses the young Hunter after overhearing his criticism and deliberately switches to casual speech. |
| 청년 | 진태경 | frightened junior Hunter to celebrated senior Hunter | you | fearful and deferential | The young Hunter uses 당신 while asking whether Jin is really the person he recognizes from the media. |
| 야율목 | 진태경 | Nanman_Beast_Palace_Young_Palace_Lord_to_Han_intruder_and_Murim_Alliance_Pavilion_Master | you | formal but hostile | Asks Jin's identity and orders him to follow after learning he belongs to the Murim Alliance. |
| 진태경 | 야율목 | Fire_Dragon_Pavilion_Pavilion_Master_to_Nanman_Beast_Palace_Young_Palace_Lord | Mok | casual, teasing, and insulting | Calls him rude and later addresses him as 목아 while jokingly claiming they are friends. |
| 요희 | 흑웅 | Yao great chieftain to Yi great chieftain | big brother | seductive and falsely affectionate | Uses 오라버니 to flatter and manipulate Heugung. |
| 흑웅 | 요희 | Yi great chieftain to Yao great chieftain | my dear | adoring and deferential | Responds to Yohi's manipulation with open infatuation. |
| 요희 | 진태경 | Yao great chieftain to Murim Alliance pavilion master | Jin Taekyung | casual and probing | Identifies him by his full name while allowing him to keep the mask on. |
| 진태경 | 요희 | Fire Dragon Pavilion pavilion master to Yao great chieftain | you | guarded and blunt | Answers Yohi's probing questions directly while warning her about Ju Hwaran. |
| 진태경 | 백호 | human ally to intelligent spiritual beast | you | casual and familiar | Converses with White Tiger after interpreting its warning. |
| 흑웅 | 진태경 | Nanman great chieftain to Central Plains ally and covert contact | you | cautious and informal | Heugung uses 자네 in private Sound Transmission while explaining the missive and Baeksang's alleged collusion. |
| 진태경 | 흑웅 | Central Plains investigator to covert informant and prospective witness | Heugung | blunt and confrontational | Jin questions Heugung's reliability, challenges his claims, and demands proof. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 688
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Heugung.md

# Heugung (흑웅)

- **Safe through:** Chapter 687
- **Aliases:** Beast Miao King
- **Role:** Heugung is the secret identity of the Beast Miao King, a Supreme Peak master and long-term Dark Heaven contingency who concealed himself through the Bone-Shrinking Technique.
- **Personality:** Heugung is calculating, patient, ruthless, and obsessive, masking coercion and strategic intent behind warmth and romantic devotion toward Yohi.
- **Voice:** Heugung speaks with warm enthusiasm and genuine, openly devoted affection toward Yohi.
- **Relationships:** Heugung is obsessed with Yohi and is willing to threaten her and the Yao people to force her compliance while secretly serving the Southern Heaven Demon Empress.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 688
- **Aliases:** Blazing Flame Divine Dragon; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang's publicly acknowledged Disciple, the Fire Gate Clan's nineteenth successor, and the Pavilion Master of the Fire Dragon Pavilion within the Murim Alliance, a Supreme Peak master with the Heavenly Martial Physique and Force, a publicly recognized S-rank-level Hunter who formally retains an A-rank license, and an escaped prisoner who is currently unconscious under the disguised Beast Miao King's control.
- **Personality:** Hungry, self-aware, dryly observant, pragmatic under pressure, and willing to risk himself for people he has accepted as real. Treats impossible situations like games until their human cost becomes undeniable.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, Jeok Cheongang is his Master, Mungyeong was his recent instructor, Cheongpung is his trusted companion and only true martial rival, Choi Minwoo is his subordinate and trusted manager of media and official arrangements, Ju Hwaran is a trusted Fire Dragon Pavilion member who followed him to Nanman, Chuck Hagel is an American operative allied with him in the covert anti-terror campaign, his mother and sister Hayeon are among those he protects, the Skeleton King is his friend and ally, Xiao Shen regards him as an older brother after Jin saved him, and Jin-ho is his older friend and trusted confidant.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 688
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Muyaho.md

# Muyaho (무야호)

- **Safe through:** Chapter 686
- **Aliases:** White Tiger
- **Role:** Muyaho is Yayul Mok's enormous white tiger companion and a renowned Nanman spiritual creature.
- **Personality:** Muyaho is intelligent enough to understand speech, wary of threats, and strongly food-motivated.
- **Voice:** Muyaho communicates through growls, roars, and gestures rather than human speech.
- **Relationships:** Muyaho is Yayul Mok's cherished companion and returned to Jin with Heugung and Yohi after carrying them through the darkness.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 654
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

### Yayul Mok.md

# Yayul Mok (야율목)

- **Safe through:** Chapter 679
- **Aliases:** None
- **Role:** Yayul Mok is the non-Han Young Palace Lord of the Nanman Beast Palace, a spear-wielding warrior who rides a white tiger and speaks Han Chinese haltingly but capably.
- **Personality:** Protective of Nanman Beast Palace livestock, quick-tempered toward trespassers, and capable of restraint once he recognizes legitimate authority.
- **Voice:** Blunt, commanding, and formal-polite toward strangers, becoming openly insulting when provoked.
- **Relationships:** Yayul Cheok is the Beast Miao King and his father, Baeksang is his father's sworn younger brother, and Yayul Mok has risked his position and life to rescue Jin Taekyung, entrusting Muyaho to Jin while he remains behind with the Seven Miao Tigers.

### Yohi.md

# Yohi (요희)

- **Safe through:** Chapter 687
- **Aliases:** None
- **Role:** Yohi is the female great chieftain of the Yao people, one of Nanman's four great tribes, and is currently incapacitated under Heugung's control after learning his identity and Dark Heaven's coercive plan.
- **Personality:** Yohi is charismatic, proud, perceptive, and fiercely resistant to Heugung's betrayal and coercion.
- **Voice:** Not established.
- **Relationships:** Yohi leads the Yao people, hates Heugung after his betrayal, and is being coerced to support his false account by the threat against Boshan and her people.

## Korean source

```text
＃689화



툭. 투둑.

차갑다.

그것이 눈을 뜬 요희가 떠올린 첫 생각이었다.

그리고 멍하니 이마 위로 떨어지는 물방울을 바라보던 그녀의 뇌리에, 잠시 잊고 있던 기억들이 하나둘씩 떠올랐다.

‘이건.’

이제야 기억난다. 자신이 누구인지. 어떤 삶을 살았는지. 요서부에서 무슨 일이 있었으며, 독혈지에서 무엇을 보았는지.

그리고…….



‘사랑하오, 요희.’



떠올리는 것만으로도 몸서리쳐지는 어느 사내의 얼굴과 목소리. 그의 뒤에 쓰러져 있는 거대한 백호와 한 청년의 모습.

그 모든 것들이.

“흡……!”

번개처럼 상체를 일으킨 요희는 입술 사이로 뛰쳐나오려는 비명을 간신히 삼켰다.

마침내 쓰러지기 전의 기억을 모두 떠올린 그녀는, 경계심과 두려움에 사로잡혀 주위를 둘러보았다.

‘이곳은 어디지?’

알 수 없는 공간이었다. 흐릿한 어둠과 주위에 내려앉은 적막. 이렇다 할 빛이 없어 모든 것을 제대로 분간할 수는 없지만, 사방이 가로막혀 있다는 것만은 확실했다.

마치 누군가 준비한 감옥처럼.

‘흑웅.’

아니, 흑웅이라는 이름을 훔친 자.

삶 자체가 거짓이었던 사내를 떠올린 요희는 본능적으로 허리춤을 더듬었다.

만일을 대비하여 언제나 요대처럼 두르고 다니던 연검(軟劍)을 찾기 위해서였지만, 그녀의 바람과는 달리 손에 닿는 것은 피와 흙으로 젖은 비단뿐이었다.

‘아. 그때.’

정체 모를 약에 취해 연검을 놓쳤던 것이 기억났다.

처음부터 해약(解藥)을 복용하지 않았으니, 당연히 공력도 여전히 금제되어 있는 상태…….

“어?”

자신도 모르게 소리를 흘린 요희는 황급히 입을 틀어막았다. 하지만 숨기지 못한 놀라움은 동그랗게 뜨인 눈에 고스란히 드러났다.

‘어떻게?’

애써 마음을 가라앉힌 요희는 혹시나 하는 마음에 두 번, 세 번에 걸쳐 자신의 몸을 파악했고, 이내 확신할 수 있었다.

‘공력의 금제가…… 풀려 있어.’

그건 틀림없는 사실이었다. 온갖 영약을 섭취하며 축적한 공력이 하단전에 충만한 것을 느낄 수 있었으니까.

문제는 왜, 그리고 어떻게라는 의문이었다.

‘나를 비롯한 모두가 흑웅에게 사로잡혔을 텐데.’

요희로서는 도무지 이해할 수 없는 상황이었다.

이 밀폐된 공간에 홀로 남겨져 있는 것도, 금제가 풀려 있는 것도.

분명 마지막 순간, 흑웅을 막을 수 있는 것은 아무도 없었다.

상당한 중상을 입은 진태경은 최소 며칠간은 깨어나지 못할 상태였고, 능히 절정 고수 한 사람의 몫을 해내는 영물인 백호는 불의의 기습으로 목숨이 경각에 달해 있었으니까.

단환의 영향으로 검 한번 휘둘러 보지 못한 채 쓰러진 그녀는 말할 것도 없다.

‘그런데 어떻게 금제가 풀린 상태일 수 있지?’

심지어 그 흔한 밧줄이나 쇠사슬로 포박당해 있던 것도 아니다. 비록 요희의 무공이 높은 편이 아니라고는 해도 절정 초입의 경지.

이건 암천의 소행이라 보기에는 너무나도 어설프고, 이상한 조치였다.

‘혹시.’

마른침과 함께 뒷말을 삼킨 요희는 조심스럽게 자리에서 일어나 주위를 자세히 살폈다.

그사이 어둠에 익숙해진 눈과 공력이 더해지자, 향상된 안력(眼力)은 어둠 너머의 광경을 읽어 냈다.

‘이건…….’

그리고 자신이 서 있는 공간의 정체를 확인한 순간, 요희는 숨이 턱 막히는 것을 느꼈다.

거대한 공간이었다. 한 사람을 가두기 위해 만들어졌다고는 믿을 수 없는.

그러나 단지 넓기만 했다면 지금처럼 숨이 막히지는 않았을 것이다. 얼핏 짐작해도 반경 수백여 장에 달할 것 같은 면적은 중요하지 않다.

문제는 차갑고 축축한 암석이 바닥부터 벽. 그리고 천장까지 사방을 감싸고 있다는 것이었다.

마치 누구도 출입할 수 없는 철옹성처럼.

‘이곳은 도대체.’

요희가 주위를 가득 메운 암석과 그 위를 뒤덮은 굵은 넝쿨을 바라보며 할 말을 잃은 순간이었다.

솨아아아.

어디선가 불어온 바람에 넝쿨이 흔들렸다.

입을 벌린 채 전신을 스치는 서늘한 바람을 맞던 요희는, 문득 머리 위로 떨어져 내리는 무언가를 느끼고 손을 뻗었다.

스륵. 툭.

가느다란 손가락 사이에 잡힌 무언가.

섬단 같은 머리카락을 스치며 떨어져 내린 그것의 정체는 넝쿨에서 떨어져 나온 잎사귀였다.

독혈지에서 봤던 것과는 달리, 생명력으로 충만한 푸른 잎사귀.

바로 그때였다.

멍하니 그것을 내려다보던 요희의 뇌리에, 한 줄기 벼락이 스쳐 지나간 것은.

‘잠깐. 바람?’

밀폐된 공간이라면 바람이 불 수 없다. 이건 봉쇄되어 있지 않은 틈새가 있다는 뜻이다.

그것도 저 굵은 넝쿨들을 흔들 정도의 강한 바람이 불어올 만큼 커다란 틈새가.

그러나 요희의 짐작과 달리, 아무리 찾아보아도 틈새는 찾아볼 수 없었다.

‘이럴 리가 없는데.’

사방을 가로막은 암석을 만져도 보고, 공력을 실어 후려치기도 했다.

그뿐인가. 혹시나 하는 마음에 익혀 본 적도 없던 벽호공(壁虎功)을 따라 하여 넝쿨을 타고 올라가기까지 했다.

저 위에 이곳을 탈출할 수 있는 틈새가 있을까 싶어서.

하지만 결국 모든 시도는 수포로 돌아갔다.

이제는 암천에 의해 사로잡혔다는 절망감이 아닌, 이해할 수 없는 공간에 들어왔다는 막막함이 들 정도로.

‘하다못해 출구도 없다는 건 말이 안 돼.’

말 그대로였다. 깨어난 직후 어림잡아도 두 시진이 넘는 시간을 헤맨 요희였지만, 틈새는 고사하고 출구 비슷한 것도 찾지 못했다.

그럼 누가, 어떻게 자신을 이곳에 가뒀단 말인가.

망연자실해진 요희는 털썩 주저앉아 석벽에 등을 기댔다. 등을 타고 전해지는 따뜻하고 푹신한 감촉에 기분이 한결 나아졌다.

“응?”

뭔가 이상한데.

잠시 눈을 깜빡이던 요희는 기댄 자세 그대로 슬그머니 뒷목을 젖혔다.

그리고 흐릿한 어둠 속에서 자신을 내려다보는 청백색 눈동자와 시선이 마주쳤다.

“아.”

- 크릉.

순간 내려앉은 숨 막히는 침묵.

천천히 몸을 일으킨 요희는 자신의 등 뒤에 절벽처럼 자리 잡은 암벽과 뭔가에 잘린 듯 상반신만 불쑥 튀어나와 있는 거대한 백호를 번갈아 바라봤다.

그리고 생각했다.

‘뭐지 이거.’

요희는 애써 침착하게 현재 상황을 정리했다.

첫째. 이곳은 정체를 알 수 없는 거대한 공간이다.

둘째. 마치 절벽 안에 갇힌 것처럼 하늘까지 암벽에 가로막혀 있고, 출구도 보이지 않는다.

셋째. 그 암벽에서 몸통이 반쯤 잘린 백호가 나타났다. 아니, 갑자기 솟아났다.

넷째. 이런 상황에서 답은 둘 중 하나다.

꿈. 아니면 저승.

요희는 망설임 없이 암벽에 머리를 박았다.

쿵.

골이 울리는 와중에도 깨지 않는 걸 보면 후자가 틀림없었다.

그도 그럴 것이, 유령처럼 상반신만 둥둥 떠 있는 저 백호의 모습은 제법 낯이 익었으니까.

‘쟤, 걔잖아.’

은빛이라 불러도 될 만큼 새하얀 털에 청백색 눈동자.

틀림없다. 소궁주 야율목이 애지중지하는 그 백호가.

이미 죽었어야 할 무야호가 다친 곳 하나 없이 멀쩡히, 그리고 천연덕스럽게 고개를 갸우뚱거리는 모습에 요희는 이곳이 저승이라는 걸 확신했다.

‘어쩐지 출구가 없더라니.’

몰랐다. 저승은 처음이라서.

잔뜩 꼬여 있던 실타래가 풀리는 듯한 기분. 마침내 찾아온 깨달음과 함께 요희의 어깨가 들썩이기 시작했다.

“흑. 흐윽. 흑웅 이 씨이발 새끼…….”

남만에 닥친 위기? 요족의 대족장으로서 지켜야 할 체면?

그게 무슨 상관인가. 이미 죽어 버렸는데.

지금 그녀를 지켜보는 시선이라고는 반 토막 난 호랑이 유령밖에 없다.

거기에 더해 이십 년 전 돌아가신 어머니까지 떠올리니 눈물이 줄줄 흘렀다.

“흐억. 흐어어어엉!”

흡사 맹수의 포효와도 같은 울음소리에, 혹시 동족이었나 하는 표정으로 요희를 바라보던 무야호가 다가와 눈물을 핥아 주었다.

- 크르릉.

얼굴 전체를 쓸어올리는 까슬까슬한 촉감.

이미 유령이 된 것치고는 너무 감각이 생생한 거 아닌가 싶었지만, 생각해 보면 죽은 뒤 감각이 없어진다는 이야기도 저승 안 가 본 놈들이나 하던 소리다.

요희는 무야호의 푹신한 털에 얼굴을 파묻고 엉엉 울었다.

적어도 부드럽고 살랑거리는 무언가가 손에 잡히기 전까지는.

덥석.

- 하악.

처음에는 우느라 신경도 안 썼고, 그다음에는 이게 뭔가 싶었다.

그리고 무야호가 토해 낸 날 선 울음소리에 고개를 들었을 때, 요희는 볼 수 있었다.

자신의 손에 잡힌 길고 새하얀 백호의 꼬리를.

‘뭐야, 꼬리였네. 난 또 뭐라고.’

내심 중얼거린 요희는 다시 털 사이에 얼굴을 묻었고, 잠시 후 다시 고개를 들었다.

뒤통수를 후려친 한 가지 충격적인 사실 때문이었다.

‘잠깐. 꼬리가 왜 있어.’

평상시라면 하등 이상할 것 없는 일이었다. 평범한 호랑이도, 심지어는 요서부 곳간에 득실거리던 쥐새끼들에게도 꼬리는 달려 있었으니까.

그러나 조금 전만 해도 상체만 둥둥 떠다니던 백호 유령이 완전체로 거듭났다는 것은, 요희에게 있어 완전히 다른 이야기였다.

‘설마?’

황급히 자리에서 일어난 요희가 무야호가 처음 모습을 드러냈던 암벽을 향해 손을 뻗었다.

탁.

지금껏 살펴본 바와 같이 차갑고 단단하다. 두께를 짐작할 수도 없고 틈새 따위는 보이지도 않는다.

하지만 실망하기에는 일렀다.

‘내가 모르는 뭔가가 있어. 분명히.’

침착함을 되찾은 이성이 말하고 있었다.

여기는 꿈속도, 저승도 아니라고. 단지 사람의 머리로 쉽게 이해할 수 없는 기기묘묘(奇奇妙妙)한 상황일 뿐이라고.

그리고 이러한 요희의 생각을 읽은 것처럼, 그녀의 주위를 맴돌던 무야호가 움직이기 시작했다.

- 그르릉.

낮은 울음소리를 흘린 거대한 백호가 하체를 비스듬히 굽힌다.

맑은 청백색 눈동자에 담긴 뜻을 어렴풋이 알아차린 요희가 설마 하는 표정으로 물었다.

“타라는 거니? 네 등에?”

- 크릉.

“하.”

영특하다고는 들었지만, 이 정도일 줄이야.

새삼스럽게 눈앞의 백호를 바라본 요희는 조심스럽게 녀석의 등에 올라탔다.

새하얀 터럭을 붙잡자 커다란 앞발이 암벽을 향해 내밀어졌다.

저벅.

워낙 덩치가 크니 한 걸음만으로도 암벽이 코앞까지 다가왔고, 요희는 눈을 질끈 감았다.

‘제발.’

마음속으로 간절히 뇌까린 그 순간.

쏴아아악!

마치 어딘가로 빨려 들어가는 듯한 기이한 감각과 함께, 요희는 천천히 눈을 떴다. 그리고 자신도 모르게 탄성을 내뱉었다.

“아.”

한없이 밝고, 따뜻했다.

어둠 대신 빛이. 차가운 암벽 대신 생기를 내뿜는 나무가. 넝쿨 대신 온갖 꽃들로 가득한 그곳은 완전히 새로운 세상이었다.

요희가 잠깐이나마 모든 상황을 잊고 평화와 아름다움에 젖을 만큼.

“이, 이곳은……?”

말꼬리를 흐리는 요희의 물음에, 무야호도 이번만큼은 대답하지 않았다.

새하얀 백호의 신형이 한 치의 망설임도 없이 초목과 꽃이 어우러진 길을 향해 쏘아졌다.

타닥, 쉬이이익!

전신을 감싸며 흩어지는 시원한 바람. 동시에 빠르게 스쳐 지나가는 풍경 너머에서는 수많은 각양각색의 동물들이 그들을 호기심 어린 눈빛으로 바라보고 있었다.

까마득히 높은 나무에 둥지를 튼 산새. 우거진 풀숲 속에서 함께 햇빛을 즐기고 있던 노루와 맷돼지.

그리고 이 어울리지 않는 한 쌍이 기댈 수 있도록 자신의 몸을 빌려주고 있는 곰까지.

‘세상에. 내가 지금 뭘 본 거지?’

그러나 요희의 마음속에 울려 퍼진 생각은 얼마 지나지 않아 순식간에 지워졌다.

먹이사슬이 무시되는 이유? 모른다. 아니, 중요하지도 않다.

그저 이 공간에 존재하는 것만으로도, 그저 모든 것이 당연하게만 느껴졌다.

‘이건. 이건 정말 말도 안 돼.’

불현듯 사술(邪術)이라는 두 글자가 요희의 뇌리를 스친 그 순간.

영원히 이어질 것 같던 길이 끝나고 작은 연못이 모습을 드러냈다.

그리고…… 그곳에 한 사람이 있었다.

“진태경!”

틀림없다. 바로 그다.

균형 잡힌 근육질의 체구와 상반신에 걸친 붉은 갑옷. 멀리서도 분간할 수 있을 정도로 확연히 눈에 띄는 그는, 맑은 물에 반쯤 잠긴 채 쓰러져 있었다.

이제 남은 거리는 불과 십여 장 남짓.

하지만 다급한 요희의 마음과는 달리, 지금껏 쉼 없이 앞으로 나아가던 백호의 발걸음은 제자리에 못 박힌 듯 움직이지 않았다.

- 크르릉.

마치 누군가를 부르는 듯한 낮은 울음소리. 순간 무언가를 느끼고 청백색 눈동자를 따라 고개를 돌린 요희는 볼 수 있었다.

아니, 보기도 전에 느낄 수 있었다.

솨아아아아.

알 수 없는 기운을 품은 서늘한 바람과 함께, 지금껏 본 적 없는 거대한 나무로부터 푸른 잎사귀가 쏟아져 내린다.

그리고 그 순간.

스윽.

거목이 드리운 드넓은 그늘 아래에서, 어둠을 닮은 흑호(黑虎)가 몸을 일으켰다.
```

## Final English reading copy

```markdown
# Chapter 689

Drip. Drip.

It was cold.

That was the first thought that occurred to Yohi when she opened her eyes.

As she stared blankly at the drops of water falling onto her forehead, memories she had briefly forgotten began returning one by one.

*This is…*

Only now did she remember. Who she was. What kind of life she had lived. What had happened at the Western Yao Estate, and what she had seen in the Poisonblood Grounds.

And…

*“I love you, Yohi.”*

Just remembering the face and voice of that man made her shudder. Behind him lay the massive White Tiger and a young man.

All of it—

“Gasp!”

Yohi shot upright like lightning, barely swallowing the scream that tried to escape between her lips.

She had finally recalled everything that had happened before she collapsed. Overcome by fear and wariness, she looked around.

*Where am I?*

It was an unfamiliar space. Blurred darkness and silence that had settled all around her. There was no real light, making it impossible to distinguish anything clearly, but one thing was certain: she was blocked in on every side.

As though someone had prepared a prison.

*Heugung.*

No—the man who had stolen the name Heugung.

Remembering the man whose entire life had been a lie, Yohi instinctively groped at her waist.

She was looking for the flexible sword she always wore wrapped around her waist like a belt in case of emergencies. But contrary to her hopes, all her hand found was silk soaked with blood and dirt.

*Ah. Back then.*

She remembered losing her flexible sword after being drugged by an unidentified substance.

She had never taken the antidote in the first place, so naturally, her internal energy remained sealed…

“Huh?”

Yohi unconsciously let out a sound and hurriedly covered her mouth. But the surprise she had failed to conceal was plainly visible in her wide, round eyes.

*How?*

After forcing herself to calm down, Yohi examined her body once, twice, then a third time, just in case.

She soon became certain.

*The seal on my internal energy… It’s gone.*

There was no doubt. She could feel the internal energy she had accumulated by consuming all kinds of elixirs filling her lower dantian.

The problem was why—and how.

*Everyone, including me, should have been captured by Heugung.*

Yohi could not understand the situation at all.

Not why she had been left alone in this sealed space, nor why the seal on her internal energy had been removed.

At the final moment, no one had been capable of stopping Heugung.

Jin Taekyung had suffered severe injuries and would not wake for at least several days. And the spiritual creature White Tiger, which was fully capable of matching a Peak master, had been on the verge of death after an unexpected ambush.

There was no need to mention Yohi, who had collapsed without even being able to swing her sword once because of the pill’s effects.

*Then how can the seal be gone?*

She had not even been bound with the usual rope or chains. Even if Yohi’s martial arts were not particularly impressive, she was still at the early stage of the Peak realm.

This was far too clumsy and strange a measure to have been Dark Heaven’s doing.

*Could it be…?*

Yohi swallowed the words that followed with a dry gulp, then carefully rose and examined her surroundings.

By then, her eyes had grown accustomed to the darkness. Once she added her internal energy to the mix, her enhanced vision began to make out what lay beyond it.

*This is…*

The moment she confirmed the nature of the space where she stood, Yohi felt the breath catch in her throat.

It was enormous—too enormous to believe it had been made to imprison a single person.

But if it had merely been wide, it would not have left her so breathless. The area, which seemed to stretch several hundred zhang in every direction, was not important.

The problem was that cold, damp stone covered everything around her, from the floor to the walls and even the ceiling.

Like an impregnable fortress that no one could enter or leave.

*What in the world is this place?*

Yohi was staring speechlessly at the rock filling the space and the thick vines covering it when—

Swoooosh.

The vines swayed in a wind that blew in from somewhere.

Yohi stood with her mouth open, feeling the cool breeze brush over her entire body. Then she suddenly sensed something falling from above and reached out.

Rustle. Tap.

Something landed between her slender fingers.

It had brushed against her fine strands of hair before falling, and its identity was simple: a leaf that had broken off from one of the vines.

Unlike the leaves she had seen in the Poisonblood Grounds, this one was green and brimming with life.

That was when a bolt of realization flashed through Yohi’s mind.

*Wait. Wind?*

If this were a sealed space, no wind could blow through it.

That meant there had to be an opening.

And not just any opening. It had to be large enough for a powerful wind to blow through and shake those thick vines.

But contrary to Yohi’s guess, she could not find a gap no matter how thoroughly she searched.

*That’s impossible.*

She touched the stone blocking her on every side and struck it with her internal energy.

That was not all. On the off chance it might help, she even imitated the Wall Lizard Technique, a martial art she had never learned, and climbed up the vines.

Perhaps there was a gap above that would allow her to escape.

But in the end, every attempt came to nothing.

She no longer felt the despair of having been captured by Dark Heaven, but rather the helpless bewilderment of finding herself in an incomprehensible place.

*There has to be an exit, at the very least.*

And that was exactly how it was.

Yohi had wandered around for more than two shichen after waking up, yet she had not found anything resembling an exit, let alone a gap.

Then who had imprisoned her here—and how?

Overcome with despair, Yohi slumped down and leaned her back against the stone wall.

The warm, soft sensation that traveled up her back made her feel slightly better.

“Hm?”

Something was strange.

After blinking for a moment, Yohi slowly tilted her head back without changing her position.

And in the faint darkness, her eyes met a pair of blue-white eyes looking down at her.

“Ah.”

—Grrr.

A suffocating silence descended in an instant.

Yohi slowly rose to her feet, looking back and forth between the cliff-like rock wall behind her and the massive White Tiger, whose upper body protruded from it as though the rest of its body had been cut away.

Then she thought:

*What is this?*

Yohi did her best to calmly organize the situation.

First. This was an enormous space of unknown origin.

Second. Just like she was trapped inside a cliff, the sky was blocked off by rock walls, and there was no visible exit.

Third. A White Tiger with half its body cut off had appeared from the rock wall. No—it had suddenly burst out of it.

Fourth. In a situation like this, there were only two possible answers.

A dream.

Or the afterlife.

Yohi did not hesitate. She slammed her head against the rock wall.

Thud.

The inside of her skull rang, but she did not wake up.

Which meant it had to be the latter.

And no wonder. The sight of that White Tiger floating around with only its upper body showing was strangely familiar.

*It’s him.*

Snow-white fur, white enough to be called silver, and blue-white eyes.

There was no mistake. It was the White Tiger cherished by the Young Palace Lord, Yayul Mok.

Muyaho should already have been dead. Yet here it was, perfectly healthy, without a single injury, calmly tilting its head to one side.

That convinced Yohi that this was the afterlife.

*No wonder I couldn’t find an exit.*

She had not known. This was her first time in the afterlife.

It felt as though a hopelessly tangled ball of thread were finally coming undone. As enlightenment arrived at last, Yohi’s shoulders began to shake.

“Sniff. Sob. You fucking son of a bitch, Heugung…”

The crisis facing Nanman? The dignity she was supposed to uphold as Great Chieftain of the Yao people?

But what did any of that matter?

She was already dead.

The only gaze watching her now belonged to a half-severed tiger ghost.

And when she remembered her mother, who had died twenty years ago, tears began streaming down her face.

“Waaah! Waaaaah!”

At the cry that sounded almost like the roar of a wild beast, Muyaho approached her. Wearing an expression that seemed to ask whether she might have been one of its kind, the White Tiger began licking her tears.

—Grrr.

Its rough tongue swept across her entire face.

It did seem strange that her senses were so vivid for someone who had already become a ghost, but now that she thought about it, people who claimed the dead lost all sensation were probably just people who had never been to the afterlife.

Yohi buried her face in Muyaho’s soft fur and sobbed.

At least, that was what she did until her hand grasped something soft and swishing.

Grab.

—Hiss!

At first, she had been too busy crying to pay attention. Then she wondered what it was.

When she lifted her head at Muyaho’s sharp cry, Yohi saw it.

The long, snow-white tail of the White Tiger was clutched in her hand.

*What? It’s a tail. I thought it was something else.*

Yohi muttered inwardly and buried her face in the fur again.

A moment later, she lifted her head once more.

One shocking fact had struck her in the back of the head.

*Wait. Why does it have a tail?*

Under normal circumstances, there would have been nothing strange about it. Ordinary tigers had tails. Even the rats swarming through the storerooms at the Western Yao Estate had tails.

But the fact that the White Tiger ghost, which had been floating around with only its upper body visible moments ago, had now become whole was an entirely different matter to Yohi.

*Could it be?*

Yohi hurriedly rose and reached toward the rock wall where Muyaho had first appeared.

Tap.

Just as she had discovered while examining it, the stone was cold and hard. She could not guess its thickness, and there was no visible gap.

But it was too soon to be disappointed.

*There’s something here that I don’t know about. There has to be.*

Her reason, now that she had regained her composure, told her so.

This was neither a dream nor the afterlife. It was simply a bizarre, uncanny situation that could not easily be understood by the human mind.

As though it had read Yohi’s thoughts, Muyaho, which had been circling her, made its move.

—Grrrr.

The massive White Tiger bent its lower body at an angle.

Yohi vaguely understood the meaning in its clear blue-white eyes and asked with a doubtful expression.

“You want me to ride you? On your back?”

—Grrr.

“Hah.”

She had heard that it was intelligent, but she had never imagined it was this intelligent.

Yohi looked at the White Tiger before her with renewed amazement, then carefully climbed onto its back.

When she gripped its snow-white fur, the tiger extended one massive forepaw toward the rock wall.

Clomp.

It was so enormous that a single step brought the rock wall right in front of them. Yohi squeezed her eyes shut.

*Please.*

At the moment she silently repeated the plea with all her heart—

Swoooosh!

Along with a strange sensation, as though she were being sucked into somewhere, Yohi slowly opened her eyes.

An involuntary exclamation escaped her lips.

“Ah.”

It was endlessly bright and warm.

Light instead of darkness. Trees overflowing with life instead of cold rock walls. A place filled with every kind of flower instead of vines.

It was an entirely new world.

For a moment, Yohi was so immersed in its peace and beauty that she forgot everything else.

“W-What is this place…?”

Yohi let her question trail off, but this time, Muyaho did not answer.

The snow-white White Tiger shot forward without hesitation, heading down a path where flowers and plants grew together.

Tap-tap. Swoosh!

A refreshing wind scattered around them, wrapping around their entire bodies. At the same time, beyond the scenery rushing past them, countless animals of every shape and color watched them with curious eyes.

Mountain birds had built nests in trees that stretched impossibly high. A roe deer and a wild boar basked together in the sunlight amid the thick grass.

There was even a bear lending the mismatched pair its body to lean against.

*Good heavens. What did I just see?*

But that thought echoing through Yohi’s mind was erased in an instant.

Why was the food chain being ignored? She had no idea.

No—it did not matter.

Simply by existing in this space, everything felt completely natural.

*This… This is truly impossible.*

It was then that two words suddenly flashed through Yohi’s mind.

*Dark arts.*

At that moment, the path that had seemed as though it would continue forever came to an end, revealing a small pond.

And there—

Someone was there.

“Jin Taekyung!”

There was no mistake.

It was him.

His well-balanced, muscular body and red armor covering his upper body stood out clearly even from a distance. He was collapsed, half-submerged in the clear water.

Only about ten zhang remained between them.

But contrary to Yohi’s desperate urgency, the White Tiger’s paws, which had moved forward without pause until now, were fixed in place as though nailed to the ground.

—Grrrr.

It was a low growl, as though calling out to someone.

Yohi sensed something and turned her head in the direction of Muyaho’s blue-white gaze.

She saw it.

No—she sensed it before she even saw it.

Swoooosh.

Along with a cool wind carrying an unknown energy, green leaves began raining down from an enormous tree unlike any she had ever seen.

And at that moment—

Rustle.

Beneath the wide shadow cast by the great tree, a Black Tiger that resembled the darkness rose to its feet.
```
