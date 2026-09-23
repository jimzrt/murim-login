<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0865.txt",
      "sha256": "c11d98e0d70af703d5e40bb079aedfd0352a8f1a3421728e34faf1805a81cdbc",
      "bytes": 12992
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "41cb6df70541c0f7343909f460b179d9038766f4b01f75c32c0bb4d6c54c2fc5",
      "bytes": 1211
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "4c101b31c65ea71d45efd4357ef39f4e35dc7c82b77dbe6d7cdd92374a1106dc",
      "bytes": 229215
    },
    {
      "path": "characters/Baek Yeon.md",
      "sha256": "0cadffbc4194c8872c78274f55d6b19b9ffaf4fddcc41423f3e82eadf61764f0",
      "bytes": 719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "c966c068e072dfb410e775bf32072f87142cd6a0ca474d24a17670bdf3b82da6",
      "bytes": 759
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "963f0827d081a2fea69bc0b5c42bbe4f9da3f36177828007442577553a3c3e00",
      "bytes": 791
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "7d2e212f85198c90006216de8d9c830aa5ff62433fd5a44284dc410d64cd5097",
      "bytes": 1378
    },
    {
      "path": "characters/Jeong Hogun.md",
      "sha256": "8b2047cdf7d2f94dac2cef8eba27e3f973823ff54cd1169823dd092d03488e9a",
      "bytes": 771
    },
    {
      "path": "characters/Jung Ho.md",
      "sha256": "3bf7bd50c64cfee449e7678c7f09308dd4c7f7340b771cddd6800a4a4a53d147",
      "bytes": 699
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "898649a25c56a25081111f3ba091859c70d6fc77fb05a8b0e574869c65d6965c",
      "bytes": 876
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2828ea7bee972440f65017b5509bb1115b51d80c6fc97bc319b084093d131e7f",
      "bytes": 255571
    }
  ],
  "estimated_tokens": 10144
}
-->

# Durable State Update — Chapter 865

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 865. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 865. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 865,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 865,
    "continuity_sources": [865],
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
    "Prince Shangshan and his party are inside the imperial palace under Baek Yeon’s escort; Baek has ordered that nobody leave.",
    "The Emperor postponed Prince Shangshan’s audience until the next day without giving a reason.",
    "Baek Yeon ordered Jeong Hogun to surveil the party while leaving openings for someone to approach.",
    "Baek Yeon’s earlier assignment has not succeeded; its nature is unstated.",
    "Shangshan will not seek Baek Yeon’s punishment because Baek serves the Emperor, not him."
  ],
  "continuity_sources": [
    863,
    864
  ],
  "open_questions": [
    "Why did the Emperor postpone Prince Shangshan’s audience, and what does he intend for the prince?",
    "What was Baek Yeon’s earlier assignment, and who has so far eluded it?",
    "Who is meant to approach Shangshan’s party through the surveillance gaps?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 864,
  "temporary_decisions": [
    "Render 동창 as “East Depot.”",
    "Render 금의위 as “Embroidered Uniform Guard” and 금위군 as “Imperial Guards.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 공자      | **Young Master**                                                |
| 백연 | **Baek Yeon** | Commander of the Embroidered Uniform Guard. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 정호군 | **Jeong Hogun** | Commander of the Embroidered Uniform Guard force confronting Jin. |
| 정호 | **Jung Ho** | Middle-aged Shaolin martial monk leading the traveling group. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 그분 | **that person** | Unidentified figure whom Jihoon reveres and credits with disabling cameras and microphones. |
| 촌각 | **moments** | Short intervals disappearing from Jeok's day. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 황족 | **Huang tribe** | Nanman tribe involved in a recently settled dispute. |
| 궁인 | **palace attendant** | Former Inner Palace attendant expelled by Baeksang. |
| 호야 | **Hoya** | Name called by the fleeing tribesman while searching for someone. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 백연 | 정호군 | commander to subordinate | you | direct and commanding | Uses 네 while testing Jeong Hogun’s obedience. |
| 홍진 | 백연 | imperial aide confronting a senior military officer | you | angry and confrontational | Uses 당신 in an indignant outburst. |

## Listed compact profiles

### Baek Yeon.md

# Baek Yeon (백연)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Baek Yeon is the Commander of the Embroidered Uniform Guard and a military officer trusted by the Emperor.
- **Personality:** Politically assured and controlled, he asserts imperial authority while tactically conceding the prince’s authority and enforcing protocol with ruthless decisiveness.
- **Voice:** Not established
- **Relationships:** He commands the Embroidered Uniform Guard and serves the Emperor; he orders Jeong Hogun to surveil Prince Shangshan’s party while leaving openings for an approach, and treats Taekyung as a dangerous potential obstacle.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 864
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, trusts Jin Taekyung to keep the prince safe, and has unresolved ties to former East Depot associates.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 864
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeong Hogun.md

# Jeong Hogun (정호군)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Jeong Hogun is a Thousand Captain of the Embroidered Uniform Guard and a highly skilled martial artist whose force includes dozens of Peak masters.
- **Personality:** Disciplined and resolute, he presents loyalty to the Emperor's command as the foundation of his force's actions.
- **Voice:** Formal and rigid, emphasizing duty to imperial authority.
- **Relationships:** A Thousand Captain in the Embroidered Uniform Guard under Baek Yeon’s command, he is ordered to surveil Prince Shangshan’s party while leaving openings for someone to approach; he says he would give his life to obey an imperial command.

### Jung Ho.md

# Jung Ho (정호)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Middle-aged Shaolin martial monk and Master of Shaolin's Discipline Hall who leads the traveling group and wields a Zen staff hung with prayer beads.
- **Personality:** Humble, observant, principled, and concerned with the safety of commoners.
- **Voice:** Formal, restrained, and admonitory, with Buddhist phrasing.
- **Relationships:** Unnamed is his young Martial Uncle; he leads the Shaolin monks traveling with him, addresses Sama Pyo as a Benefactor, and is recognized by Jin Taekyung as Park Jung Ho, a former Garam Middle School classmate.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 864
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, and seeks candid counsel when making difficult decisions.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃865화



사람의 몸과 정신은 활시위와 같다.

팽팽하게 당겨졌다가, 이내 일거에 풀어지는.

긴장감이 풀리면 피로가 몰려오기 마련.

수많은 위기를 헤쳐 온 나조차도 그러한데, 하물며 이제 겨우 열두세 살에 불과한 어린아이라면 말할 것도 없었다.

달칵.

행여 자신의 어린 주군이 잠에서 깰까, 조심스럽기 그지없는 손길로 문을 닫은 홍진이 내게 속삭였다.

“많이 피곤하셨나 봐. 금세 잠드셨어요.”

닫힌 문 틈새로 들려오는 새근거리는 숨소리.

상산왕이 완전히 잠든 것을 확인한 나는 창밖을 힐끗 내려다보았다.

저 아래 일렁이는 횃불들 사이로, 황금빛 갑주를 걸친 채 철탑처럼 서 있는 금의위들의 모습이 보였다.

‘시벌놈들. 적당히 어두워졌으면 정시 퇴근 좀 하지.’

물론 내 바람은 이루어지지 않을 것이다.

지금껏 겪어 본 바에 의하면, 저놈들은 명령을 수행하기 위해서라면 야근이 아니라 죽음까지 불사할 놈들이니까.

무림인이라는 족속들도 하나같이 제정신이 아니지만, 금의위는 그야말로 천자에게 맹목적인 충성을 바치는 사냥개나 다름없었다.

“그렇게 지켜본다고 달라지는 건 없어요. 촌각도 자리를 비우지 않을 테니까.”

마치 포위하듯 전각을 에워싼 횃불과 금의위를 살핀 홍진이 덧붙였다.

“그게 창위(廠衛)의 방식이죠.”

“창위?”

“아, 창위는 동창과 금의위를 합쳐 부르는 명칭이에요. 진 공자한테도 말했듯이 나 역시 그중 하나였고.”

물론 홍진이 과거 동창에 속했었다는 사실은 들어서 알고 있지만, 아직 묻고 싶은 이야기가 많이 남아 있다.

그리고 홍진은 내 마음을 읽은 것처럼 먼저 입을 열었다.

“드디어 우리끼리만 남았으니, 잠깐 이야기 좀 할까요?”

그렇게 말해 준다면야 나야 고맙지.

고개를 끄덕인 나는 홍진과 함께 아래층으로 걸음을 옮겼다.

이미 금의위도, 그들이 감시원으로 붙여 준 것이나 다름없는 궁인(宮人)들도 내보낸 상황.

하지만 전각 내부에서 벌어지는 모든 일을 손바닥 내려다보듯이 관조할 수 있는 내가 있음에도, 홍진은 상산왕이 홀로 남겨지는 것을 극도로 경계하는 모습을 보였다.

“진 공자, 괜찮을까?”

“걱정하실 필요 없습니다. 저도 가까이에 있고, 무엇보다 만약을 대비해 무진이 녀석을 전하 곁에 남겨 뒀으니까요.”

“응. 그래서 더 불안해.”

“…….”

혁무진이 저 말을 못 들어서 다행이라는 생각을 하며 아무도 없는 방에 들어섰다.

황궁 소유의 전각답게 내부는 넓었고, 고풍스러운 집기 사이로 은은한 향이 감돌았다.

‘무엇보다 가장 좋은 점은, 도청 가능성이 전혀 없다는 거지.’

현대에서는 중요한 이야기를 할 때마다 혹시 모를 도청을 우려했었는데, 무림은 재래식이라 맘 편히 대화를 나눌 수 있다.

“이제야 좀 숨이 트이네. 안 그래요?”

홍진도 나와 얼추 비슷한 생각을 한 모양이었다. 어두운 내부를 밝히기 위해 불붙인 촛대를 창가에 가져다 놓은 그는, 자리에 앉자마자 지친 얼굴로 입을 열었다.

“진 공자 입장에서도 묻고 싶은 게 많겠지만, 우선 나부터 말해도 될까요?”

“원하시는 대로.”

“그를 필요 이상으로 자극하지 마세요. 절대.”

확실한 지칭은 없었지만, 나는 홍진이 말하는 ‘그’가 누구인지 즉각 깨달았다.

“백연 말입니까?”

“맞아요. 금의위 지휘사 백연. 그자와는 최대한 거리를 두는 게 좋아요.”

왜냐고는 굳이 묻지 않았다.

아니, 물어볼 필요조차 없다.

상대는 바로 그 금의위의 수장이자 대단히 뛰어난 초절정 고수. 거기에 더해 천자에게 가장 신임받는 무관이다.

그중 하나만 해당해도 경계해야 할 부분은 차고 넘치는데, 셋 모두 가졌다면 두말할 것도 없다.

하지만…….

“그러기에는 이미 너무 좁혀진 것 같은데요. 그 거리가.”

내 대답에 홍진이 한숨을 내쉬었다.

“그건 나도 잘 알아요. 모든 상황을 이 두 눈으로 똑똑히 봤으니까. 그저…… 지금부터라도 조심하라는 뜻이에요.”

표정과 목소리, 말하는 태도에서까지 묻어 나오는 우려.

내가 아는 홍진도 배짱 하나만큼은 어디 가서 뒤지지 않는 인물이다.

환관들로 이루어진 동창은 금의위와 함께 황제의 인간 청소기 역할을 하는 살벌한 집단.

바로 그 동창에서도 제법 고위직이었던 것으로 짐작되는 만큼 산전수전 다 겪었을 테고, 실제로 정호군을 위시한 여타 금의위들이나 동창의 환관들을 상대하면서도 비웃음마저 내비쳤었다.

백연이 나타나기 전까지는.

“제가 모르는 또 다른 이유라도 있습니까?”

그리고 다음 순간 들려온 홍진의 대답에, 나는 그의 우려를 즉각 이해할 수 있었다.

“삼만 명. 백연이 지난 정변(政變)에 잡아 죽인 이의 숫자예요.”

“……!”

“이미 후계 구도에서 밀려난 네 번째 황자가 어떻게 대국의 황위(皇位)을 손에 넣을 수 있었을까? 단지 본연의 능력이 출중해서? 아니에요. 그 정도로는 부족해. 명분도 사람도. 혼자만의 힘으로는 절대 천자가 될 수 없지.”

가쁘게 말을 쏟아낸 홍진이 품에서 꺼낸 곰방대를 물었다.

얼마 지나지 않아 독한 냄새와 함께 피어오르는 연기 속, 유독 어두워 보이는 얼굴을 한 그가 말을 이었다.

“백연은 내가 황궁에 들어오기 훨씬 이전부터 이미 금의위의 수장이었어요. 젊은 시절부터 선황(先皇) 폐하의 신임을 한 몸에 받았고, 한때는 황태자 전하의 무술 교두를 맡기도 했었지.”

“황태자라면, 바로 그……?”

“맞아요. 그래서 백연이 사 황자를 도와 정변을 일으켰을 때, 모두가 경악을 금치 못했어요. 다른 누구도 아닌 그가 선황과 황태자를 배반할 줄은 몰랐으니까.”

후우우.

홍진이 뱉어 낸 연기가 모락모락 솟아올랐다. 마치 희뿌연 안개 같은 연기 사이로 그가 기억하는 과거가 스쳐 지나가는 듯했다.

“모든 것이 그야말로 순식간에 시작되고, 찰나에 끝났어요. 그 움직임이 얼마나 은밀했는지 동창조차 손 쓸 수 없었지. 아니, 예상치도 못했기에 당했다고 해야 맞으려나?”

깊은 밤 시작된 정변은 새벽 어림에 끝났다.

거센 말발굽 소리는 동틀 무렵까지 황도를 울렸고, 비명은 끊이지 않았다.

“정변은…… 정말이지, 소름 돋을 만큼 완벽했어요. 황제 폐하의 생신을 축하하기 위해 모든 문무백관은 물론 천하 각지에 흩어져 있던 황족들까지 한자리에 모인 상황이었고, 만일의 상황을 대비한 방비는 그 어느 때보다 철저했죠. 단 한 가지만 빼면.”

동네 이장도 아니고 무려 한 대륙의 주인인 황제의 탄생일.

인산인해를 이루던 그 날의 상황이 눈앞에 선명하게 그려지는 듯했다. 황궁을 철통처럼 에워싼 그들의 휘황한 금빛 갑주도.

“……금의위. 금의위가 황궁의 방비를 맡았군요.”

내 말을 들은 홍진이 쓴웃음을 지으며 고개를 끄덕였다.

“네, 맞아요.”

이미 모든 것이 철저하게 준비되어 있었다.

백연과 그를 따르는 금의위는 순식간에 황궁을 장악했고, 하나같이 경악을 금치 못하는 좌중 속에서 홀로 일어선 사 황자는 담담한 얼굴로 자신을 위해 준비된 무대에 올랐다.

대국의 역사가 뒤바뀌는 순간이었다.

“그리고…… 숙청이 시작되었죠.”

누구도 예상치 못했던 무대가 끝났지만, 그 누구도 자리를 떠나지 않았다. 아니, 떠날 수 없었다.

처음 자리에 참석할 때만 해도 관객에 지나지 않았던 그들은, 곧바로 이어진 새로운 무대의 배우가 되어야만 했다.

“곧장 순응했던 이들은 살아남았고, 반발하는 이들은 금의위가 관리하는 형옥(刑獄)으로 끌려갔어요. 황족들의 상황은 그나마 나았지. 처음에는 단순한 구금으로 그쳤으니까.”

이미 연로했던 황제, 아니 선황은 거처에 갇혔다. 황태자 부부를 비롯한 황족들 역시 예외일 수는 없었다.

그들은 숨 쉴 틈 없는 철저한 감시를 받으며 하루하루를 버텼고, 사방을 가로막은 높은 담 너머로 밤낮없이 들려오는 비명에 몸을 떨었다.

곧 다가올 자신들의 차례를 기다리며.

“그 과정에서 무수한 이들이 죽었어요. 멸문지화(滅門之禍)를 당한 가문도 헤아릴 수 없을 만큼. 그리고…….”

말꼬리를 흐린 홍진이 덧붙였다.

“당시 숙청을 진두지휘했던 사람이 바로 금의위 지휘사. 아니, 혈사자(血使者) 백연이었죠.”

“혈사자…….”

“들을 때마다 생각하는 거지만, 퍽 어울리는 별호야. 안 그래요?”

홍진은 입꼬리를 말아 올렸지만, 그 힘없는 미소는 금세 흔적도 없이 사라졌다.

“진 공자. 당시의 나는 아무것도 할 수 없었어요. 역모를 알아차리지 못했으니 신하로서 무능(無能)했고, 그 모든 것을 그저 바라만 볼 수밖에 없었으니 무력(無力)했지. 하지만 그때나 지금이나 한 가지는 변치 않았어요.”

툭.

담뱃재를 털어 낸 홍진이 말을 이었다.

어린 왕이 새근새근 잠들어 있을 천장 너머를 꿰뚫어 보듯이 바라보며.

“난 상산왕 전하를 지켜야 해요. 이건 선황 폐하께서 남기신 유지(遺志)인 동시에, 무능하고 무력했던 신하가 바치는 마지막 충성이기도 하지.”

물 흐르듯 이어지던 목소리가 끊겼다.

무거운 침묵 속에서 조금 전 들었던 이야기를 곱씹던 나는 불쑥 입을 열었다.

“글쎄요. 충성심과는 조금 다른 것 같은데요.”

“응?”

“신하가 주군을 지키려는 것과, 부모가 아이를 생각하는 마음은 엄연히 다릅니다. 그리고 제가 지금까지 본 도지휘동지의 모습은 후자에 가까운 것 같네요.”

“……하고 싶은 말이 뭐죠?”

“간단합니다. 상산왕 전하가 마냥 지켜 줘야 할 어린아이가 아니라는 거죠.”

내 말을 들은 홍진이 한숨을 내쉬었다.

“진 공자, 미안하지만 그분은 아직 어려요. 이제 고작 열셋이라고요.”

“맞습니다. 고작 열셋이죠. 나는 새도 떨어트리는 금의위 지휘사를 고개 숙이게 만들고, 눈앞에서 사람이 죽어 나가도 평정심을 유지할 수 있는.”

“……!”

가끔. 어쩌면 꽤 자주.

사사로운 감정에 사로잡힌 이들은 때때로 잘못된 판단을 내리고는 한다.

‘설령 그 사람이 산전수전 다 겪은 동창의 환관이라 해도.’

나는 굳어 버린 홍진의 눈을 응시하며 말을 이었다.

“상산왕 전하는 누군가가 지켜 줘야만 하는 어린아이가 아닙니다. 그분은 이미 오래전부터 왕이었어요. 다만 아직 완전히 무르익지 않았을 뿐이지.”

“진 공자, 당신.”

“그저 생존을 원한다면, 당장 내일이라도 황제에게 엎드려 빌면 되겠죠. 도무지 무슨 죄를 지었는지는 모르겠으나 이번 한 번만 살려 달라고. 물론 그 간절한 청이 황제의 촉촉한 감수성을 자극한다는 전제하에.”

“……!”

“하지만 도지휘동지께서도 내심은 다른 생각을 하고 계시잖습니까. 안 그래요?”

굳은 얼굴로 나를 응시하던 홍진이 메마른 목소리로 물었다.

“왜 그렇게 생각했죠?”

“황제에게 간과 쓸개까지 빼 주며 비위를 맞춰야 할 판국에, 감히 강호의 무뢰배들을 황궁에 들였으니까. 동창과 금의위의 앞에서 도발적인 언사를 행했으니까. 그리고…….”

나는 문득 뒤를 돌아보며, 천천히 말을 이었다.

“이 야심한 밤에, 초대받지 않은 손님을 금의위의 눈을 피해 이곳까지 들였으니까.”

그 순간.

화륵, 훅.

홍진이 방에 들어서자마자 피워올렸던, 창가에 놓인 세 개의 촛불이 동시에 꺼진다.

텅 빈 허공에서 나타난 검은 인영(人影)과 홍진을 번갈아 바라보던 나는 입을 열었다.

“그래서, 소개는 언제쯤 해 줄 겁니까?”
```

## Final English reading copy

```markdown
# Chapter 865

A person’s body and mind are like a bowstring.

Drawn taut, then released all at once.

Once the tension lets up, exhaustion is bound to catch up with you.

That was true even for me, after weathering countless crises. For a child who was barely twelve or thirteen, it went without saying.

*Click.*

Careful not to wake his young lord, Hong Jin closed the door with the utmost care and whispered to me,

“He must have been exhausted. He fell asleep in no time.”

A soft, even breathing came through the crack in the closed door.

Once I was sure Prince Shangshan was fast asleep, I glanced out the window.

Down below, amid the swaying torchlight, the Embroidered Uniform Guard stood like iron towers, clad in golden armor.

*You bastards. It’s gotten dark enough already. Why don’t you clock out on time for once?*

Of course, my wish wouldn’t come true.

From what I’d seen so far, those guys would risk not just overtime but their lives to carry out an order.

Murim martial artists were all crazy in their own way, but the Embroidered Uniform Guard were hunting dogs, blindly loyal to the Son of Heaven.

“Watching us like that won’t change anything. They won’t leave their posts for even a moment.”

Hong Jin surveyed the torches and guards surrounding the pavilion as if they were laying siege to it, then added,

“That’s how the Changwei operate.”[^1]

“Changwei?”

“Oh, it’s a collective name for the East Depot and the Embroidered Uniform Guard. As I told Young Master Jin, I was once part of one of them.”

I’d heard that Hong Jin used to belong to the East Depot, of course, but there was still plenty I wanted to ask him.

And as if he’d read my mind, Hong Jin spoke first.

“Now that it’s finally just the two of us, shall we talk for a bit?”

I’d be grateful if he did.

I nodded, and Hong Jin and I walked downstairs together.

We’d already sent away the Embroidered Uniform Guard, as well as the palace attendants who were more or less there to keep an eye on us for them.

Even though I could survey everything happening inside the pavilion as easily as looking down at my palm, Hong Jin was still fiercely wary of leaving Prince Shangshan alone.

“Young Master Jin, do you think it’s all right?”

“There’s no need to worry. I’m nearby, and more importantly, I left that rascal Mujin with His Highness as a precaution.”

“Right. That’s why I’m even more uneasy.”

“……”

Thank goodness Hyuk Mujin hadn’t heard that. I stepped into an empty room.

As befitted a pavilion belonging to the imperial palace, it was spacious, and a faint fragrance drifted among the antique furnishings.

*The best part is, there’s no chance of anyone bugging us.*

Back in the modern world, whenever I had an important conversation, I worried that someone might be listening in. Murim was old-fashioned, so I could talk without a care.

“Finally, I can breathe a little. Don’t you think?”

Hong Jin seemed to have had much the same thought. He brought a lit candelabra to the window to brighten the dark room, then sat down and spoke, looking tired.

“I’m sure you have a lot you want to ask me, Young Master Jin, but could I speak first?”

“Go ahead.”

“Don’t provoke him more than necessary. Whatever you do.”

He hadn’t said exactly who he meant, but I immediately knew who Hong Jin was talking about.

“Baek Yeon?”

“That’s right. Baek Yeon, Commander of the Embroidered Uniform Guard. It’s best to keep your distance from him.”

I didn’t ask why.

There was no need.

He was the head of the Embroidered Uniform Guard and an exceptionally skilled Supreme Peak master. On top of that, he was the military officer most trusted by the Son of Heaven.

Any one of those would be reason enough for caution. All three together left nothing to discuss.

But…

“I think that distance has already gotten pretty short.”

Hong Jin sighed at my answer.

“I know. I saw everything with my own two eyes. I’m just saying you should be careful from now on.”

His concern came through in his expression, his voice, even the way he spoke.

The Hong Jin I knew wasn’t lacking in nerve. The East Depot, made up of eunuchs, was a ruthless organization that acted as the Emperor’s human-cleanup crew alongside the Embroidered Uniform Guard.

Judging by the fact that he’d held a fairly high position there, he must have been through all sorts of hell. In fact, when dealing with Jeong Hogun and the other guards, or the East Depot eunuchs, he’d even shown open contempt.

That is, until Baek Yeon appeared.

“Is there another reason I don’t know about?”

The moment I heard Hong Jin’s answer, I understood his concern.

“Thirty thousand. That’s how many people Baek Yeon had arrested and killed in the last coup.”

“……!”

“How did the fourth prince, already sidelined in the struggle for succession, manage to seize the throne of a Great Nation? Just because he was exceptionally capable? No. That wouldn’t have been enough. He needed a cause, and he needed people. No one can become the Son of Heaven by their own strength alone.”

Hong Jin spoke rapidly, then took the long-stemmed tobacco pipe from inside his clothes and put it to his mouth.

Before long, smoke rose with a pungent smell. Hong Jin continued, his face looking especially dark through the haze.

“Baek Yeon was already head of the Embroidered Uniform Guard long before I entered the imperial palace. He had the late Emperor’s full trust from a young age, and at one point he even taught the Crown Prince martial arts.”

“The Crown Prince—you mean the one…?”

“That’s right. So when Baek Yeon helped the fourth prince stage a coup, everyone was stunned. No one thought he’d betray the late Emperor and the Crown Prince—not him.”

*Hoooo.*

Smoke curled up from Hong Jin’s lips. Through it, the past he remembered seemed to drift before us like a pale fog.

“Everything began in an instant and ended just as quickly. The coup was so secretive that even the East Depot couldn’t do a thing. No—maybe it’s more accurate to say we were caught off guard because we never saw it coming.”

The coup began in the dead of night and was over around dawn.

The pounding of hooves echoed across the imperial capital until daybreak, and the screams never stopped.

“The coup was… perfect enough to make your skin crawl. Every civil and military official had gathered to celebrate His Majesty the Emperor’s birthday, along with members of the imperial family from every corner of the land. Security was tighter than ever, in case anything happened. Except for one thing.”

It wasn’t the birthday of some village headman, but of the Emperor, ruler of an entire continent.

I could almost see it all before me: the packed crowds that day, and the dazzling golden armor of the guards who had sealed off the imperial palace.

“……The Embroidered Uniform Guard. They were in charge of the palace defenses.”

Hong Jin gave a bitter smile and nodded.

“Yes. That’s right.”

Everything had been prepared down to the last detail.

Baek Yeon and the guards who followed him took control of the imperial palace in an instant. As everyone looked on in shock, the fourth prince alone rose to his feet and stepped onto the stage prepared for him, his expression calm.

It was the moment the history of the Great Nation changed.

“And then… the purge began.”

The unexpected spectacle was over, but no one left their seats. No—no one could.

The people who had arrived as nothing more than spectators were forced to become actors in the next performance.

“Those who submitted at once survived. Those who resisted were dragged off to the prisons controlled by the Embroidered Uniform Guard. The imperial family had it a little better, at least. At first, they were only confined.”

The Emperor—no, the late Emperor—was already old. He was locked inside his residence. The Crown Prince and his wife, and the rest of the imperial family, were no exception.

They endured day after day under relentless watch, trembling at the screams that rang out day and night beyond the high walls surrounding them.

Waiting for their turn to come.

“Countless people died in the process. More families than anyone could count were destroyed. And…”

Hong Jin let his voice trail off, then added,

“The man who led the purge was the Commander of the Embroidered Uniform Guard. No—the Blood Envoy, Baek Yeon.”

“The Blood Envoy…”

“I’ve always thought that sobriquet suits him rather well. Don’t you?”

Hong Jin curled his lips into a smile, but it was feeble and vanished without a trace almost immediately.

“Young Master Jin. Back then, I couldn’t do anything. I was incompetent as a subject: I failed to detect the treason. And I was powerless: all I could do was watch it happen. But there’s one thing that hasn’t changed, then or now.”

*Tap.*

Hong Jin knocked the ash from his pipe and continued.

He looked up as if trying to see through the ceiling, beyond which the young prince was sleeping peacefully.

“I must protect His Highness Prince Shangshan. It’s the late Emperor’s final wish, and the last act of loyalty from a servant who was both incompetent and powerless.”

His smooth, flowing voice came to a halt.

Turning over what I’d just heard in my mind, I suddenly spoke.

“I’m not sure that’s really loyalty.”

“Hmm?”

“Wanting to protect your lord and wanting to protect a child as a parent are two very different things. And from what I’ve seen of you, Deputy Military Commissioner, I’d say the latter is closer.”

“What are you trying to say?”

“It’s simple. His Highness Prince Shangshan isn’t just a child who needs someone to protect him.”

Hong Jin sighed at my words.

“Young Master Jin, I’m sorry, but he’s still young. He’s only thirteen.”

“That’s right. Only thirteen—and already able to make the Commander of the Embroidered Uniform Guard, a man whose influence could knock birds from the sky, bow his head. Already able to keep his composure while people die right in front of him.”

“……!”

Sometimes. Maybe even fairly often.

People caught up in their personal feelings make the wrong call.

*Even if that person is a eunuch from the East Depot who’s been through hell and back.*

I held Hong Jin’s frozen gaze and continued,

“His Highness Prince Shangshan isn’t a child who needs someone else to protect him. He’s been a king for a long time already. He just hasn’t fully come into his own yet.”

“Young Master Jin, you…”

“If all he wanted was to survive, he could throw himself at the Emperor’s feet as soon as tomorrow and beg for his life. He could plead, ‘I don’t have the faintest idea what crime I’ve committed, but please spare me just this once.’ Assuming, of course, that his desperate plea manages to stir the Emperor’s tender heart.”

“……!”

“But you have something else in mind, don’t you, Deputy Military Commissioner?”

Hong Jin stared at me, his face set, then asked in a dry voice,

“What makes you think that?”

“At a time when you should be bending over backward to please the Emperor, you dared to bring martial-world ruffians into the imperial palace. You dared to taunt the East Depot and the Embroidered Uniform Guard. And…”

I suddenly turned around and continued slowly,

“On this dark night, you brought an uninvited guest all the way here, past the eyes of the Embroidered Uniform Guard.”

At that moment—

*Fwoosh. Whoosh.*

The three candles Hong Jin had lit as soon as he entered the room went out all at once.

I looked back and forth between Hong Jin and the black figure that had appeared out of thin air, then spoke.

“So, when are you going to introduce us?”

[^1]: *Changwei* is a collective term for the imperial court’s East Depot and Embroidered Uniform Guard.
```
