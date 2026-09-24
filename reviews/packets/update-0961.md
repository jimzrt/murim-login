<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0961.txt",
      "sha256": "f23475155ada6893882048f0a93feffb056ddb913a9471d64a789c0f3552668c",
      "bytes": 13003
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "aceb9c85c7c1bf99debaf500de87dbfa0e67dc8cc8a38e514d0e806c86e9ea81",
      "bytes": 2309
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "ff5b5206798ca2c45ec6dcc084fc376e02e91696419ae72ce39f481882b60323",
      "bytes": 235018
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "7b397ca6972de64bbf0c6ba996289a5c128b11b5ed7154838d01994355b7267a",
      "bytes": 1007
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "ede24cc3a05862278bcd2c02b5d46074c7f0dbce91f5f718655f40099f220283",
      "bytes": 759
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "6920a94613b98820aadb380f4abc5c179d4cacacde8b077237a9bf61d7abbdb0",
      "bytes": 1343
    },
    {
      "path": "characters/Wipeng.md",
      "sha256": "cdf753076d937adc3b204567912d8e2d0e4cb9dddacc75c90f752ac508604bd7",
      "bytes": 954
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "f3891a6f1dc69b187910650fe3f1d1ef0807d3efb213de9337d593761b5d84c5",
      "bytes": 268981
    }
  ],
  "estimated_tokens": 10250
}
-->

# Durable State Update — Chapter 961

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
1 and safe_through 961. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 961. Profile updates may replace only one
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
  "chapter": 961,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 961,
    "continuity_sources": [961],
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
    "The battle at Eight Spring Gorge is ongoing; Jin Mukyung, Wipeng, and Cheol Mubaek are fighting the Demon Bird amid the Shanxi defenders’ battle against the steppe army.",
    "The Demon Bird is the impostor who wore Chinggen’s face, an elderly and overwhelmingly powerful martial artist who left Temur alive to control the western tribes.",
    "The Dongting Fisherman died fighting the impostor; the Jin Family considers itself indebted to him. His training helped Wipeng and Cheol Mubaek coordinate against the Demon Bird.",
    "Jin Mukyung’s Sword Energy forced the Demon Bird back, and the Demon Bird recognized Mukyung’s technique as One Strike.",
    "Jamukha ordered the Keshik at the gorge to wear down the defenders while limiting losses to his personal guard; three of his commanders of a hundred have died.",
    "Temur chose survival over loyalty and feels guilty that his actions led his followers to slaughter; Jamukha threatened him into obedience.",
    "The Emperor remains gravely ill with Blood Soul Gu; saving him requires him to die once, and Taekyung’s treatment remains unresolved.",
    "Jang Sam remains unconscious after his sudden rise in level and attack on Taekyung; the improved Temporary Strength Pill’s source, effects, and distribution remain unknown.",
    "The Martial God’s identity and connection to the chosen one and the Bow Saint remain unknown.",
    "The Eastern Heaven Demon Lord’s papers and silk pouch remain unexplained.",
    "Taekyung resolved to trust his allies rather than bear every burden alone."
  ],
  "continuity_sources": [
    959,
    960
  ],
  "open_questions": [
    "How will the battle at Eight Spring Gorge end, and can the defenders defeat the Demon Bird?",
    "Who gave Jang Sam the silk pouch, and what are the improved pill’s effects and distribution?",
    "What is the Martial God’s identity and connection to the chosen one and the Bow Saint?",
    "What do the Eastern Heaven Demon Lord’s papers and silk pouch contain?",
    "What will become of Temur and the followers he led into battle?"
  ],
  "safe_through": 960,
  "temporary_decisions": [
    "Taekyung intends to keep the pocket watch for half a month before deciding whether to give it to Mujin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 위팽     | **Wipeng**         |
| 철무백    | **Cheol Mubaek**   |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 검법     | **sword technique**                              |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 생사결    | **life-and-death duel**                          | Explicitly lethal                                     |
| 정파     | **orthodox faction**                             |                                                       |
| 사파     | **unorthodox faction**                           |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 제자     | **Disciple**                                 |
| 일격     | **One Strike**                         |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 노부      | **this old man / I**                                            |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 권기 | **Fist Energy** | Projected martial energy produced by a fist technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 강기 | **Force** | Generic manifestation of concentrated martial energy; distinct from Sword Force. |
| 마두 | **fiend** | Demonic martial masters from the Great Faction War era. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 영물 | **spiritual creature** | Known non-human creature contrasted with unheard-of monsters. |
| 신병이기 | **divine weapon** | Jin's description of White Flame. |
| 육부 | **Six Ministries** | The central government ministries. |
| 케식 | **Keshik** | Elite warriors serving the Golden Clan. |
| 검귀 | **Sword Demon** | Title used for the kind of swordsman Mukyung is said to resemble. |
| 마조 | **Demon Bird** | Title given by the revealed impostor who wore Chinggen’s face. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진무경 | 마조 | hostile opponents | you | blunt and insulting | Mukyung directly insults the Demon Bird, refusing to call him Master. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 960
- **Aliases:** Tiger of Mount Heng
- **Role:** Cheol Mubaek is the ninth-generation successor of the Shura Annihilating Fist and the Peak master known as the Tiger of Mount Heng, now out of seclusion and active in the rebuilding of the Mount Heng Sword Sect.
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; considers Jin Taekyung, Jin Mukyung, and Hyuk Mujin Benefactors for protecting Seowol and enabling the Mount Heng Sword Sect's survival, and vows to repay them even at the cost of his life; feared and respected by the Mount Heng Sword Sect's senior figures

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 960
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 960
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Jin Mukyung is the second son of the Jin Family of Taiyuan, a Peak-level swordsman known as the Heaven Shaking Sword, and Commander of the Heaven Shaking Squad.
- **Personality:** Reserved and disciplined, Jin Mukyung is devoted to swordsmanship and seeks strength in service of his family.
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Jin Wikyung is his older brother and the Lesser Family Head who formed the Heaven Shaking Squad in his honor; Jin Taekyung is his younger brother, and Mukyung cherishes his promise to reunite with him.

### Wipeng.md

# Wipeng (위팽)

- **Safe through:** Chapter 960
- **Aliases:** Ghost Sword; God of Drinking
- **Role:** Jin Wikyung’s personal guard and Commander of the Jin Dragon Squad; one of the Jin Family’s three Peak masters
- **Personality:** Loyal, observant, teasing, capable, and resigned to Jin Wikyung’s impulsive behavior. Respects the dead and urges others to live on their behalf.
- **Voice:** Weary and knowing, with dry humor when addressing Jin Wikyung or Jin Taekyung. Uses Sound Transmission when appropriate.
- **Relationships:** Trusted guard and retainer of Jin Wikyung; a reliable senior ally of Jin Taekyung. He has fought beside the Jin Family in major battles, including the conflict with Mount Heng, and remains alert to threats connected with Dark Heaven. The Human Butcher has claimed him as a personal target in a planned attack.

## Korean source

```text
＃961화



어둠을 가르며 피어오르는 은은한 혈광(血光)을 본 순간, 항산호 철무백은 비로소 깨달았다.

마조라는 생소한 별호로 스스로를 소개한 저 비대한 노인의 정체를.

“혈혼비마(血魂肥魔).”

신음처럼 흘러나온 한 마디에 마조의 얼굴이 일그러졌다.

“너 같은 어린놈이 어찌…….”

몇 년 후면 환갑에 접어드는 철무백이었지만, 그런 노강호조차 마조의 눈에는 새파란 애송이나 다름없는 나이.

그러나 지금 이 순간 마조에게 있어 무엇보다 신경 쓰이는 것은 오랜만에 듣게 된 옛 별호 때문이었다.

혈혼비마.

살인을 사냥이라 여기며, 수많은 마인들 중에서도 유독 죽음과 피에 집착한 탓에 얻게 된 그 별호에는 조롱도 함께 포함되어 있었다.

살쪘다는 의미를 지닌 비(肥).

그 한 글자는 매번 마조의 심기를 건드렸고, 그는 언제나 자신의 감정과 본능에 충실한 사람이었다.

“그 빌어먹을 별호도 오랜만에 듣는군. 그동안 하도 많이 죽여 댔더니 이제는 노부를 알아도 모르는 척하는 놈들이 부지기수였거든.”

정파에서 보낸 추살대도, 딴에는 비위를 맞추겠답시고 연신 굽신거리던 사파 떨거지도, 심지어 한때 제법 친했던 마인들까지도 죽였다.

이유는 간단했다.

듣는 것만으로도 짜증이 솟구치는 자신의 별호를 입에 담았기 때문이다.

오죽하면 외관과는 영 어울리지도 않는, 마조(魔鳥)라는 별호를 스스로 지었겠나.

한데 항산호라는, 듣도 보도 못한 별호를 지닌 새파란 어린놈이 잠시 묻어 두었던 불쾌한 추억을 끄집어냈다.

‘감히.’

운명은 이미 정해진 것이나 다름없다.

마조는 마음속 살생부의 첫 줄에 철무백의 이름을 적으며 입을 열었다.

“네놈 같은 애새끼가 노부와 일면식이 있을 리는 없고……. 누구냐, 네 스승이?”

까득.

두 주먹을 말아 쥔 철무백이 대답했다.

“권호(拳豪).”

“권호?”

느긋한 걸음으로 다가가던 마조의 발걸음이 문득 멈췄다.

사실 물어보면서도 큰 기대는 없었다.

누군가를 죽이고 또 죽여 왔던 일생이다. 그 숫자가 일천을 넘겼을 때부터는 세지도 않고 구태여 기억할 필요도 없었다.

하지만 권호는 여전히 기억 속에 선명히 남아 있는 별호였다.

자신과 생사결을 벌이고도 살아남은, 몇 안 되는 생존자라는 점에서 더더욱.

“이런 기막힌 인연을 봤나. 네 녀석이 권호의 제자라고? 아니, 그전에 그런 몸뚱어리로 후계를 키워냈단 말이냐?”

마조는 분노도 잊은 채 너털웃음을 터트렸고, 철무백은 서늘한 목소리로 대꾸했다.

“스승님을 모욕하지 마라. 너 따위는 비교도 되지 않을 만큼 훌륭한 분이셨으니.”

“그래, 어련하겠나. 권사(拳士)로서의 생명이 끝장난 와중에도 제자를 키워 냈으니 근성 하나만큼은 인정해 주지. 양팔을 잘라 냈을 때 놈의 표정이 어땠는지 네놈도 봤어야 했는데.”

“……!”

“이거, 지금에서야 다시 보니 제법 호화로운 잔칫상이었군. 태원진가의 젊은 검귀에, 수라멸권(修羅滅拳)의 후계자까지.”

흡족한 눈빛으로 좌중을 쓸어 보는 마조의 모습에 위팽이 침을 탁 뱉었다.

“나는 안 보이나?”

“그럴 리가. 잠시 후면 죽어 나자빠져 있을 네놈의 시체가 벌써부터 눈앞에 선한데.”

“길고 짧은 건 대봐야 아는 법.”

“그런 건 나약한 것들이 지껄이는 개소리지.”

쿵.

나아간 발걸음과 함께 주름 잡힌 살집이 출렁였다.

마조는 육중한 체구와는 어울리지 않는 날카로운 눈빛으로 세 사람을 훑었다.

“자, 그럼…….”

쉭.

“누구부터 죽여 줄까.”

단 한 걸음.

수 장에 달하는 거리를 지우며 들이닥친 마조의 양손에서, 두 자루의 검이 호선을 그렸다.

마치 핏빛 발톱을 지닌 한 마리의 새처럼.

쉬이잉!



* * *



쉬쉭, 콰드드득!

광풍이 휘몰아친다.

막강한 압력이 공기를 집어삼키며 살갗을 찢었고, 굉음과 함께 솟구친 흙 알갱이와 바위의 파편은 사방을 후려쳤다.

- 이 공자!

귓가를 파고드는 위팽의 전음.

마조의 강기를 피해 연달아 물러서던 진무경은 불현듯 고개를 꺾었다.

후웅.

예리하기 그지없는 두 줄기의 바람이 목덜미를 스쳤다.

기다렸다는 듯이 기습을 피한 진무경의 모습에, 초승달처럼 휘어진 신월도(新月刀)를 꼬나 쥔 케식 두 명이 아쉽다는 듯 혀를 찼다.

그리고 그것이 그들의 마지막 모습이었다.

서걱!

핏빛 섬광이 번뜩였을 때는 이미 모든 것이 끝난 후였다.

자신들이 어떻게, 무슨 이유로 죽음을 맞이했는지도 모르는 케식들은 온순하게 쓰러졌다.

목 없는 시체가 되어 허물어지는 그들의 등 뒤에는 그 이유를 설명해 줄 한 사람이 거대한 살기를 뿜어내고 있었다.

“네놈들이 감히 내 먹잇감을 훔쳐 먹으려 들어?”

콰직!

혈혼비마. 혹은 마조.

별호와는 어울리지 않는 비대한 체구를 지닌 노인은 쓰러진 케식들의 시체를 성난 얼굴로 짓밟았다.

바로 그 순간, 등 뒤에서 들이닥치는 또 다른 먹잇감들의 존재는 까맣게 잊은 것처럼.

혹은, 신경 쓸 필요조차 느끼지 못하는 사람처럼.

“놈!”

항산호 철무백.

오래전 어느 극악무도한 마두에게 양팔을 잃은 위대한 권사의 제자이자, 벗의 외동딸을 도와 항산검문의 호법이 된 그는 노호성과 함께 일권(一拳)을 내질렀다.

후우우웅, 펑!

압축된 공기가 터져 나간다. 회전을 가미하여 쏘아진 주먹 끝에서 뻗어 나간 권기(拳氣)가 스승의 원수를 휩쓸었다.

아니, 적어도 그 순간만큼은 그렇게 보였다.

슈확!

주인을 닮아 불그스름하게 물든 장검이 공간을 갈랐다.

막아서는 모든 것을 잿가루로 만들어 버릴 것 같던 권기가 힘없이 사그라지며 흩어지는 광경에, 마조의 입가에 비웃음이 맺혔다.

“확실히 스승보다는 못하군. 내가 알던 그 수라멸권이 맞는지 의문이 들 정도야.”

그러나 마조 스스로도 알고 있었다.

수라멸권은 이백여 년 전만 하더라도 천하에서 열 손가락 안에 꼽히던 권각지공이고, 철무백의 현재 경지는 과거의 권호에 비해도 그리 큰 차이가 없다는 것을.

수라멸권이, 철무백이 부족한 것이 아니라 마조 자신이 강해졌을 뿐이라는 것을.

“오너라!”

마조는 전신의 피가 끓어오르는 것을 느꼈다.

손에 들린 두 자루의 검은 어느 때보다 가벼웠고, 먹잇감들의 움직임은 선명하면서도 느리게 보였다.

마치 아직 일어나지도 않은 미래를 읽는 것처럼, 그는 사각(斜角)에서 비스듬히 찔러 들어오는 섬광을 향해 검신을 곧추세웠다.

꽈앙!

단순히 검과 검이 맞닿은 것이라고는 생각할 수 없는 굉음.

마조는 막강한 반발력에 의해 신음을 흘리며 튕겨 나가는 위팽을 향해 비대한 신형을 내쏘았다.

흔들림 없는 확신과 함께.

‘우선 하나.’

물이 위에서 아래로 흐르고, 사람이 나이가 들면 죽음을 맞이하듯이 세상 모든 것에는 정해진 운명이 있는 법.

마조에게는 위팽의 죽음이 바로 그러한 것이었다.

나이에 비해 훌륭한 경지를 이룬 절정 고수.

귀검이라는 별호가 납득이 될 만큼 실전적인 검법을 구사하는 뛰어난 검수(劍手).

하지만 마조의 눈에 비친 위팽은 딱 거기까지였다.

노력과 운이 따른다면 십수 년 안에 초절정의 경지에 들어설지도 모르나, 그날은 결코 찾아오지 않을 터였다.

오늘 이 협곡에서 자신을 만났다는 것은, 하늘이 이미 위팽을 버렸다는 증거니까.

벽을 넘지 못한 자와 넘어선 자.

절정과 초절정의 차이는 바로 그런 것이다.

‘귀신이 되거라. 네 별호처럼.’

마조는 혈광을 번뜩이며 두 자루의 검을 휘둘렀다.

왼손에 쥔 소검은 동료를 구하기 위해 달려드는 철무백에게. 오른손에 쥔 장검은 혼신의 힘을 다해 맞서는 위팽에게.

그리고 그 격돌의 결과는, 마조가 미처 예상하지 못했던 방향으로 흘러가고 있었다.

콰득, 카가가각!

“……!”

두 자루의 검신으로부터 전해지는 적잖은 반발력.

서로 다른 세 갈래의 기운이 뒤섞여 피워 내는 그 휘황한 불꽃을 바라보는 마조의 눈동자가 크게 뜨였다.

‘뭐?’

지금 이 순간, 그가 느끼는 당혹감의 크기는 생각했던 것 이상이었다.

철무백과 위팽.

벽을 넘어서지 못한 그 하룻강아지들이, 한 끼 식사에 불과한 먹잇감들이 자신의 일격을 막았다.

하찮은 권기와 검기 따위로, 그것도 마조가 전력을 다한 검강(劍罡)에 맞서 버티고 있었다.

‘도대체 어떻게.’

마조는 타고난 살인자이자 사냥꾼이다.

그렇기에 누구보다 잘 알고 있었다.

눈앞의 먹잇감들은 무공 그 자체에 대한 깨달음도, 몸 안에 품고 있는 공력도 자신에 비하면 한참이나 떨어진다는 것을.

한데, 그 믿을 수 없는 상황이 눈앞에 펼쳐졌다.

한낱 절정 고수 따위가 수 갑자의 공력을 실어 휘두른 강기를 정면에서 맞받은, 있을 수도 없고 있어서도 안 되는 일이.

쿨럭. 촤아악.

갈라진 입술 사이로 내장 조각이 섞인 핏물이 쏟아진다.

당혹스러운 눈빛으로 굳어 버린 마조를 향해, 철무백과 위팽은 피에 젖은 이빨을 드러내며 웃었다.

핏빛 강기에 맞서 간신히 버티는 것이 고작인 지금 이 순간에도 강대한 힘을 이기지 못하고 파르르 떨리고 있는 새하얀 권갑(拳鉀)과 검신 뒤에서.

그리고 짙은 핏물로도 가리지 못한 은은한 빛을 뿜어내는 두 무림인의 애병을 본 마조는, 그제야 잠시 잊고 있던 사실 한 가지를 떠올릴 수 있었다.

초절정 고수의 강기에 대항할 수 있는 것은, 그와 같은 강기 뿐만이 아니라는 것을.

‘만년한철(萬年寒鐵)……!’

마조는 생각지도 못한 진실에 숨을 삼켰다.

어찌 알았겠는가.

긴 세월을 살아온 그조차도 손에 넣지 못했던 신병이기(神兵利器)가, 변방에 속한 산서성의 두 절정 고수의 손에 들려 있을 줄은.

동시에 감히 짐작조차 할 수 없었다.

지금 이 순간 그가 만년한철이라 생각한 저 병기가, 보이지 않는 곳에서 수백여 년간 강을 지키던 어느 영물의 뼈로 이루어진 것이라는 사실을.

그리고 예상치 못한 상황에서 그가 드러낸 빈틈은, 아직 쓰러지지 않은 누군가에게 있어 곧 기회나 다름없었다.

‘흡!’

위팽은 온 힘을 쥐어 짜내어 검을 비틀었다.

손목은 이미 부러졌고 손아귀는 너덜거렸지만, 그는 극심한 내상으로 차오르는 핏물을 삼키며 자신을 짓누르고 있는 기운을 비스듬히 흘려보냈다.

까드드득!

새하얀 검신을 타고 미끄러진 장검이 지면을 파고들었다.

검에 실려 있던 힘만큼이나, 아주 깊숙이.

푹!

뒤늦게 당혹감에서 벗어난 마조의 눈동자에 분노가 떠오른 바로 그 순간.

콰드득!

철무백이 서서히 권갑을 밀어 내던 소검을, 그 짧은 검신을 뒤덮은 강기를 움켜잡았다.

우직. 까드득.

섬뜩한 파열음과 함께 밀려드는 아득한 고통.

항거할 수 없는 거대한 기운에, 권갑 안의 살갗이 뭉개지고 뼈가 으스러진다.

만약 수신룡의 뼈로 만든 신병이기가 없었다면 강기에 닿는 순간 그의 양손은 흔적도 없이 사라졌을 터.

그러나 철무백은 결코 그것을 놓지 않았다.

형용할 수 없는 고통에 신음조차 흘러나오지 않고, 엄청난 공력을 감당하지 못한 오장육부가 뒤틀리는 와중에도 온 힘을 다해 검신을 부여잡았다.

오래전, 두 팔 없이도 자신을 가르쳤던 훌륭한 스승을 떠올리며.

또한 못난 제자를 대신하여 놈의 숨통을 끊어 줄 누군가를 기다리며.

그리고, 그 소망이 마침내 한 사람의 검에 닿았다.

솨악.

소름 끼치도록 희미한 파공성.

한 줄기 벼락처럼 나아간 섬광이, 마조를 향해 떨어져 내렸다.
```

## Final English reading copy

```markdown
# Chapter 961

The moment he saw the faint blood-red glow rising through the darkness, the Tiger of Mount Heng, Cheol Mubaek, finally understood the identity of the obese old man who had introduced himself with the unfamiliar title Demon Bird.

“Blood Soul Fat Demon.”

At the words, which slipped from Cheol Mubaek’s lips like a groan, the Demon Bird’s face twisted.

“How does a brat like you know…?”

Cheol Mubaek would turn sixty in a few years, but in the Demon Bird’s eyes, even a veteran like him was no more than a green young pup.

At that moment, though, what bothered the Demon Bird most was hearing that old title again after so long.

Blood Soul Fat Demon.

He had earned it because he considered murder a form of hunting and, among the countless fiends, was unusually obsessed with death and blood. The title had always carried a note of mockery, too.

Fat.

That single word always got under the Demon Bird’s skin. He had never been one to deny his feelings or instincts.

“It’s been a long time since I heard that damned title. I’ve killed so many people over the years that now, even when they recognize me, plenty of them pretend they don’t.”

He had killed the execution squads sent by the orthodox faction, the unorthodox rabble who’d bowed and scraped to curry favor with him, and even the fiends he’d once been fairly close to.

The reason was simple.

They’d said the title that made his blood boil just to hear.

Why else would he have given himself the title Demon Bird, a name that didn’t suit his appearance at all?

And now a green young pup with the unheard-of title Tiger of Mount Heng had dredged up those unpleasant memories he’d buried away.

*How dare you.*

His fate was all but sealed.

The Demon Bird wrote Cheol Mubaek’s name at the top of the list of people he intended to kill, then spoke.

“A brat like you couldn’t possibly have met me before… So who was your master?”

Crack.

Cheol Mubaek clenched both fists and replied.

“Fist Hero.”[^1]

“Fist Hero?”

The Demon Bird had been approaching at an unhurried pace, but now he stopped.

He hadn’t expected much when he asked.

He had spent his life killing people, over and over. Once the count passed a thousand, he stopped keeping track. There was no point in remembering them all.

But Fist Hero was still a title that remained vivid in his memory.

More so because he was one of the few who had survived a life-and-death duel with the Demon Bird.

“What a coincidence. You’re the Fist Hero’s Disciple? Wait—he raised a successor with that body?”

The Demon Bird forgot his anger and burst out laughing. Cheol Mubaek answered in a cold voice.

“Don’t insult my master. He was a far greater man than you could ever be.”

“Of course he was. Even after his life as a fist master was over, he still managed to raise a Disciple. I’ll give him credit for his grit. You should’ve seen his face when I cut off both his arms.”

“……!”

“Now that I take another look, this really is quite the lavish feast. The young Sword Demon of the Jin Family of Taiyuan—and the successor of the Shura Annihilating Fist.”

As the Demon Bird’s satisfied gaze swept over them, Wipeng spat.

“Can’t see me, either?”

“Of course I can. I can already picture your corpse lying dead in front of me in a moment.”

“You have to see how long or short it is before you can tell.”

“That’s the kind of bullshit weaklings say.”

Thud.

With each step, the old man’s heavy, wrinkled flesh rippled.

His sharp eyes looked completely at odds with his massive frame as he sized up the three men.

“Well, then…”

*Whoosh.*

“Who should I kill first?”

In a single step, the Demon Bird closed a distance of several *jang*. Two swords swept in arcs from his hands.

Like a bird with blood-red claws.

*Whoooosh!*

* * *

*Shhk—KRRRUNCH!*

A gale howled.

Mighty pressure swallowed the air and tore at their skin. Dirt and shards of rock blasted outward with a roar.

—Second Young Master!

Wipeng’s Sound Transmission pierced Jin Mukyung’s ears.

As Mukyung retreated again and again to avoid the Demon Bird’s Force, he suddenly jerked his head aside.

*Whoom.*

Two razor-sharp streams of wind skimmed past the back of his neck.

The two Keshik holding crescent-shaped sabers clicked their tongues in disappointment as Mukyung dodged their ambush, as if he’d been expecting it.

And that was the last anyone saw of them alive.

*Shhk!*

By the time a blood-red flash flickered, it was already over.

The Keshik fell quietly, never knowing how—or why—they had died.

Behind their headless bodies stood the one who could have explained it, radiating an enormous killing intent.

“You dare try to steal my prey?”

*CRUNCH!*

Blood Soul Fat Demon. Or the Demon Bird.

The old man’s massive frame didn’t suit his title. He angrily trampled the fallen Keshik’s bodies.

At that very moment, he seemed to have forgotten the other prey rushing at him from behind.

Or perhaps he didn’t think they were worth noticing.

“You bastard!”

The Tiger of Mount Heng, Cheol Mubaek.

A Disciple of the great fist master who had lost both arms to a fiend long ago, he had become a protector of the Mount Heng Sword Sect to help a friend’s only daughter. With a roar, he threw a single punch.

*Whoooooom—BANG!*

Compressed air exploded. Fist Energy shot from his spinning fist and engulfed his master’s killer.

Or at least, that was what it looked like for that one moment.

*Fwoosh!*

A long sword, stained a reddish hue like its owner, sliced through space.

The Fist Energy, which had seemed ready to turn everything in its path to ash, faded and scattered without force. A sneer touched the Demon Bird’s lips.

“You’re certainly no match for your master. I’m not even sure that’s the Shura Annihilating Fist I knew.”

But even the Demon Bird knew the truth.

Two hundred years ago, the Shura Annihilating Fist had ranked among the ten greatest fist and foot arts in the world. And Cheol Mubaek’s current realm wasn’t all that far below the Fist Hero’s, either.

It wasn’t the Shura Annihilating Fist or Cheol Mubaek who fell short.

The Demon Bird had simply grown stronger.

“Come!”

The Demon Bird felt the blood in his whole body boil.

The two swords in his hands had never felt lighter. The movements of his prey looked clear—and slow.

As if he could see a future that had yet to happen, he raised his blade toward a flash thrusting diagonally from his blind spot.

*KABOOM!*

The thunderous impact was far too loud to have come from two swords simply clashing.

Wipeng groaned as the tremendous recoil sent him flying. The Demon Bird shot his massive frame toward him.

*One first.*

As water flowed from high to low and people grew old and died, everything in the world had its own destined end.

To the Demon Bird, Wipeng’s death was just such a thing.

A Peak master who had achieved an impressive realm for his age.

An outstanding swordsman whose practical sword technique justified the title Ghost Sword.

But to the Demon Bird, that was all Wipeng was.

With enough effort and luck, perhaps he would reach Supreme Peak within a dozen years or so. But that day would never come.

Meeting the Demon Bird in this gorge today was proof that Heaven had already abandoned him.

Those who had yet to cross the wall—and those who had.

That was the difference between Peak and Supreme Peak.

*Become a ghost. Live up to your title.*

With blood-red light flashing, the Demon Bird swung both swords.

The short sword in his left hand went for Cheol Mubaek, rushing to save his comrade. The long sword in his right went for Wipeng, who was meeting him with all his strength.

But the clash that followed unfolded in a way the Demon Bird had never expected.

*CRUNCH—KRRRRANG!*

“……!”

A substantial recoil traveled up both sword blades.

The Demon Bird’s eyes widened as he watched the dazzling sparks bloom from three different streams of energy clashing together.

*What?*

The shock of what he felt was greater than he’d imagined.

Cheol Mubaek and Wipeng.

Those two young pups who hadn’t crossed the wall—prey who should have been no more than a meal—had stopped his strike.

They were holding their ground against the Sword Force he’d unleashed with all his strength, using nothing more than their puny Fist Energy and Sword Energy.

*How is this possible?*

The Demon Bird was a born killer and hunter.

That was why he knew better than anyone that his prey were far behind him—not only in their insight into martial arts, but also in the internal energy they held within their bodies.

And yet the impossible was happening right before his eyes.

A mere Peak master had met head-on the Force he’d swung with several *jiazi* of internal energy. It was something that couldn’t happen—and shouldn’t.

*Cough. Spurt.*

Blood mixed with bits of their innards poured from Cheol Mubaek’s and Wipeng’s split lips.

The Demon Bird stared, frozen with shock. Cheol Mubaek and Wipeng bared their bloodied teeth and smiled.

They were only barely holding out against the blood-red Force. Their snow-white gauntlets and sword blades trembled under its overwhelming might.

Behind them, the Demon Bird saw the faint glow coming from the two martial artists’ beloved weapons, which even the thick blood hadn’t been able to conceal. Only then did he recall something he’d briefly forgotten.

Force was not the only thing capable of standing up to a Supreme Peak master’s Force.

*Ten-Thousand-Year Cold Iron…!*

The Demon Bird swallowed at the unexpected truth.

How could he have known?

Even he, who had lived through so many long years, had never obtained a divine weapon like this. And yet such weapons were in the hands of two Peak masters from remote Shanxi Province.

At the same time, he could never have guessed the truth: that the weapons he now mistook for Ten-Thousand-Year Cold Iron were made from the bones of a spiritual creature that had guarded a river unseen for hundreds of years.

And the opening he’d left by revealing his surprise was nothing less than an opportunity for someone who hadn’t fallen yet.

*Hup!*

Wipeng summoned every last bit of his strength and twisted his sword.

His wrist was already broken, his hand mangled. But he swallowed the blood rising from his severe Internal Injury and redirected the energy bearing down on him, turning it aside.

*KRRRRUNCH!*

The long sword slid down the snow-white blade and drove into the ground.

As deep as the force behind it had been.

*Thud!*

The Demon Bird’s eyes blazed with anger as he came out of his shock—at that very instant—

*CRUNCH!*

Cheol Mubaek seized the short sword that had been slowly forcing his gauntlet back, gripping the Force shrouding its short blade.

*Crack. Krrrunch.*

A chilling sound of rupture, followed by unbearable pain.

Under the irresistible force, the flesh beneath his gauntlets was crushed and his bones splintered.

If he hadn’t had a divine weapon made from the Water God Dragon’s bones, both hands would have vanished without a trace the moment they touched the Force.

But Cheol Mubaek didn’t let go.

He couldn’t even groan through the indescribable pain. His internal organs twisted, unable to bear the immense energy, yet he clung to the blade with all his strength.

He remembered the great master who had taught him long ago, even without his arms.

And he waited for someone to kill the bastard in his stead, doing what he, an unworthy Disciple, could not.

At last, that wish reached another man’s sword.

*Shwaash.*

A faint, chilling sound as it cut through the air.

Like a bolt of lightning, a flash shot forward and descended toward the Demon Bird.

[^1]: Literally, “Fist Hero,” his master’s sobriquet.
```
