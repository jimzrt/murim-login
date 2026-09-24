<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0991.txt",
      "sha256": "c50b88c315d56fc6ffbaf0be3d536ce82f843e73249196810039ad1e66a2d44b",
      "bytes": 13077
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "a33488b9e0d31802cb17947f4cff7ba13143722342ee093b77fb749ae082c354",
      "bytes": 1083
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "d13308fe31a2c64daebd8b79b1737ef2a4f6a2f6e86338670363f6d7acf5174f",
      "bytes": 236719
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e515d8ad8200ff4da8933600e3d60a454e97ba231c7eb3ed3d4405199a36bf9e",
      "bytes": 759
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "e73e726761d69324048ea81b36058639a4fd3a9d3290cc480c5621db521ce517",
      "bytes": 1374
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "e9f52a97ae0b3eb5d424db40c20c9968dae5ff70a3023f9c6229720a0f455523",
      "bytes": 1391
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2e8b61dadbf084cecee32b110e9cf2dfcd0b5ba12bd4ff4071cf5a132aad0340",
      "bytes": 1574
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "ffbdeceda48f7c70ef2dafc2d2e21610b089912fa2002457b4c6120709644492",
      "bytes": 622
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "1cf22f09be500c14b07e0a59a3e5822a738e368eb4b5fb4796d9f5ceabc9c133",
      "bytes": 3207
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "bd5753e5df794eedf5b2ea27975a392475eb9bba5427ebd9beecb42050b7771b",
      "bytes": 273611
    }
  ],
  "estimated_tokens": 10484
}
-->

# Durable State Update — Chapter 991

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
1 and safe_through 991. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 991. Profile updates may replace only one
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
  "chapter": 991,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 991,
    "continuity_sources": [991],
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
    "Peng Cheolhu died after passing everything he had to Jin Taekyung through Transmitting Internal Energy Across the Body.",
    "Jin Taekyung underwent Bone Transformation after the transfer.",
    "Mae Jonghak regards the age as anomalous, with Dark Heaven, supernatural forces, grotesque monsters, and the Lord of Heaven at the center of growing danger.",
    "Unprecedented snowfall and rapidly changing heavenly patterns are occurring across the world.",
    "Dark Heaven is understood to threaten the entire world, and Peng Cheolhu’s death and the Eight Heavens Blood Calamity have intensified mobilization against it.",
    "Cheongpung is in Qinghai with the Slaughter Saint."
  ],
  "continuity_sources": [
    989,
    990
  ],
  "open_questions": [
    "What is behind the worldwide weather and heavenly-pattern changes?",
    "Is the upheaval a scheme laid by some unknown power, as Mae Jonghak suspects?",
    "What are Dark Heaven and the Lord of Heaven planning?"
  ],
  "safe_through": 990,
  "temporary_decisions": [],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 조필     | **Jopil**          |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 열화문    | **Fire Gate Clan**               |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 혈도     | **acupoint** / **vital point**                   | Context dependent                                     |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 큰형     | **eldest brother**                           |
| 극양                        | **Extreme Yang**      |
| 상태               | **Status**                     |
| 태원     | **Taiyuan**            |
| 노부      | **this old man / I**                                            |
| 귀가      | **your family**                                                 |
| 공자      | **Young Master**                                                |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 노환 | **infirmities of old age** | Jeok Cheongang's age-related illness. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 멸염신권 | **Flame-Extinguishing Divine Fist** | Named fist technique Taekyung announces at the chapter's end. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 리치 | **Lich** | Named Monster; fallen archmage and apex undead monster. |
| 겁화 | **hellfire** | Destructive fire energy used by Taekyung. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 제갈 | **Zhuge** | Surname used for Sir Zhuge. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 신의 | 진태경 | physician_to_benefactor | Young Master Jin | formal-polite | The Divine Physician addresses Taekyung as 진 공자 while expressing concern for his injuries. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 989
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 985
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 990
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; believes there is no absolute justice and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 990
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader; the Emperor has appointed him Marquis of Shangshan and Thousand Captain of the Embroidered Uniform Guard.
- **Personality:** Hungry, self-aware, and dryly observant; pragmatic under pressure, willing to risk himself for others, and unwilling to excuse cruelty as the inevitable price of survival.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; Peng Cheolhu regarded Taekyung as a worthy successor, inheriting all that Peng had to pass on; So Gyo says he is the chosen one spoken of by the Martial God, while the Bow Saint sought him for decades and relayed the Martial God’s message to him.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 990
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 871
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan; dead after fighting Jin Taekyung and drawing on his innate qi, with half his upper body destroyed; he left behind the Supreme Peak martial art Flame Divine Palm; he was an orphan named Jangcheon whom Jeok Cheongang rescued after an epidemic in Anhui Province and eventually accepted as his Disciple
- **Personality:** Cruel, amused by violence, motivated by both payment and the pleasure of hunting his targets; a born Slaughter Saint who rationalizes murder through Might Makes Right and feels empty when victims die
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

## Korean source

```text
＃991화



의식을 잃거나 깊은 잠에 빠졌을 때마다 모종의 꿈에 사로잡히는 것은, 내게 있어 더 이상 특별한 일이 아니다.

꿈이 곧 마음의 창구라고 했던 누군가의 말처럼, 내가 미처 떨쳐 내지 못한 고민과 남아 있는 기억들은 이리저리 뒤섞이고 합쳐져 꿈이라는 허상으로 드러나기 마련이었으니까.

결국 이 세상의 모든 일에는 원인이나 이유가 있고, 꿈 역시 다를 바 없는 것이다.

그래.

분명 그럴 터였다.

적어도 내가 알고 있던 바로는.

그런데 어째서…….

‘나는 왜, 이런 꿈을 꾸고 있는 거지?’

흐릿한 시야 속에서, 천천히 눈을 깜빡였다.

그저 몽롱하다.

소름 끼치도록 생생했던 다른 꿈들과 달리, 지금의 나는 주위를 둘러싼 허상들을 제대로 분간할 수조차 없었다.

하지만 다음 순간 불현듯 들려온 누군가의 목소리에, 뒤늦게나마 이 몽롱함의 정체를 알아차릴 수 있었다.



‘녀석, 많이 졸린 모양이구나.’



졸리다.

나는 비로소 그 사실을 인지하며 고개를 들었다.

아니, ‘들렸다’는 표현이 더욱 정확할지도 모른다.

처음부터 깜빡이던 눈의 움직임도, 지금의 고갯짓도, 그리고 지금 이 순간 달싹이는 입술 사이로 흘러나오는 목소리도 내 의지로 행해지는 것이 아니었으니까.



‘응. 나 졸려.’



물에 잠긴 듯 먹먹한 목소리였지만 하나는 알겠다.

지금의 나는 아이다.

칭얼거리는 것이 조금도 어색하게 느껴지지 않을 정도의 어린아이.

그렇게 한 가지 의문은 해결되었지만, 새롭게 떠오른 의문이 그 빈자리를 채웠다.

아이의 칭얼거림을 받아 주고 있는 저 낯선 목소리의 남자는 누구인가.

‘어디에서도 들어 본 적 없는 목소리인데.’

목소리가 무슨 주민등록증도 아니고, 듣자마자 단번에 알아차릴 수는 없겠지만 그래도 꿈속에 나타날 정도의 인물이라면 익숙해야 마땅하다.

하지만 지금의 내게는 모든 것이 낯설었다.

희뿌연 시야 속에서 들려오는 저 음성도, 노이즈 낀 TV 화면처럼 느릿느릿 재생되고 있는 이 허상도.

그리고 내 것이 아닌 입술 사이로 흘러나온 아이의 한마디를 듣는 순간, 이 알 수 없는 낯섦의 정체를 깨달을 수 있었다.



‘아버지. 나 자도 돼?’



만약 스스로의 의지로 소리 내어 말할 수 있었다면, 나도 모르게 침음성을 흘리고 말았을 것이다.

내가 마주한 진실은 그만큼 놀라우면서도 이해할 수 없는 일이었으니까.

‘아버지라고?’

아니다. 그럴 리 없다.

가장 오래된 기억의 서랍을 거꾸로 뒤집어 흔들어도 이런 기억은 존재하지 않았다.

흐릿하게나마 뇌리에 남아 있는 아버지의 목소리도, 몽롱한 시야 속에서 들려오는 사내의 음성과는 전혀 달랐다.

그러니까 이건.

‘내 기억이, 아니다.’

알 수 없는 한기가 등골을 타고 흐른 그때.

아버지라 불린 낯선 사내의 목소리가 귓가를 파고들었다.



‘좋은 꿈 꾸거라. 우리 아들.’



머리카락을 쓰다듬는 따뜻한 손길과 다정한 어투.

이내 어둠으로 곤두박질치는 시야 속에서, 사내의 마지막 한 마디가 아스라이 울려 퍼졌다.



‘……아.’



비록 흐릿하지만, 똑똑히 들었다.

아들을 향한 아버지의 음성을. 그 이름을.

그리고 생각지도 못한 충격에 머릿속 사고(思考)가 정지한 그 순간.

화아악.

칠흑 같은 어둠 너머로 쏟아져 내린 빛이, 깊은 잠에 빠진 아이를 감싸 안았다.

아니, 나를.



* * *



누군가가 내게 의식을 되찾을 때마다 무엇을 가장 먼저 보게 되느냐 묻는다면, 나는 천장이라고 대답하겠다.

혹은 호법(護法)이라는 명목으로 방 한구석에 처박혀 코까지 골며 잠든 혁무진의 모습이나, 내가 깨어날 때까지 곁을 지키고 있던 적천강의 얼굴이라든지.

하지만 이번만큼은 그 무엇에도 해당되지 않았다.

허억, 헉.

마치 용수철처럼 튕기듯 상반신을 일으켜 세운 나는 가쁘게 숨을 몰아쉬었다.

질식사 직전에 몰린다면 이런 상태일까.

겨우 되찾은 시야는 녹아내리는 촛농처럼 흐물거렸고, 사방에서 들려오는 제각각의 목소리들은 천둥과도 같이 귓가에 울려 퍼졌다.

“약왕……. 와라! 어서!”

“……장님, 조장님!”

“이게 뭐……!”

아직 꿈인가? 아니면 현실?

무엇하나 분간되지 않는 그 상황 속에서, 혼란에 사로잡힌 내가 본능처럼 다가오는 손길들을 연신 뿌리치던 그때였다.

누군가의 단단한 손아귀가 내 어깻죽지를 붙잡은 것은.

덥석.

이 와중에도 또렷하게 느껴지는 강인한 힘.

그로 인한 미약한 통증과 함께, 알 수 없는 온기가 손아귀를 통해 전해졌다.

스아아아.

한껏 경직되어 있던 몸이 부드럽게 풀렸다.

이 광활한 천하에서 오직 두 사람만이 알고 있는 혈도의 경로를 따라 흘러내리는 극양(極陽)의 기운이 누구의 것인지, 나는 그제야 뒤늦게 깨달을 수 있었다.

“……노야.”

참았던 숨과 함께 토해 낸 한 마디에, 익숙하기 그지없는 목소리가 되돌아왔다.

“잠시, 아주 잠시만 그대로 있거라.”

나는 적천강의 말에 따라 눈을 감았다.

지금 이 순간 내가 존재하는 이곳이 허상이 아닌 현실이라는 것을 인지하고, 쉴 새 없이 두방망이질 치는 심장 박동을 서서히 가라앉혔다.

그렇게 어느 정도의 시간이 흘렀을까.

마침내 눈을 뜬 나는, 고요하면서도 선명한 세상과 마주할 수 있었다.

근심 어린 눈빛으로 나를 바라보고 있는 낯익은 얼굴도.

“미련한 놈 같으니. 이제야 좀 정신이 드느냐?”

불쑥 던져진 적천강의 물음에, 잠시 머뭇거리다가 대답했다.

“어느 정도는요.”

“아직이라는 뜻이군.”

“혹시 저 한 대만 세게 때려 주실 수 있습니까?”

“뭐라?”

“한 번. 딱 한 번요. 정말 봐주는 것 없이, 진심을 담아서.”

“…….”

“부탁드립니다.”

굳은 얼굴로 부탁하는 내 모습에, 적천강이 한숨을 내쉬며 주먹을 들었다.

“오냐. 알았다.”

화륵.

삽시간에 일어난 백색 화염이 굳게 말아 쥔 주먹을 휘감으며 타오른다.

거두절미하고 멸염신권(滅炎神拳)의 일초(一招)를 쏘아 보내려는 그의 모습을 지켜보던 내가 침착하게 입을 열었다.

“엄청 뜨겁네요.”

“새삼스럽게 무슨 헛소리냐. 원래 우리 열화문 무공이 다 그렇지.”

“뜨거운 게 느껴지는 걸 보니 확실히 정신이 돌아온 것 같습니다.”

적천강이 고개를 내저었다.

“노부가 보기에는 아직이다.”

“다시 생각해 보니까 괜찮을 것 같은데요.”

“진심으로 하라며.”

“이 정도까지는 아니었습니다.”

“부탁까지 할 때는 언제고?”

“이렇게까지 진심으로 하실 거였으면 세 번까지는 거절하셨어야죠. 그게 예의 아닙니까.”

“미친놈이로고. 노부가 제갈천강이냐? 방정맞은 주둥이 그만 놀리고 딱 대라.”

말과는 달리 주먹을 거둔 적천강이 손을 까딱이자, 침상 옆 탁자에 놓여 있던 물병이 쏘아지듯 날아왔다.

“뭣 하느냐. 목부터 축이지 않고.”

“감사합니다.”

나는 숨도 쉬지 않고 가득 찬 물병을 단번에 비웠다.

차가운 냉수가 메말라 있던 목을 시원하게 쓸어내리자, 비로소 숨통이 트이는 기분이었다.

“후우.”

“왜, 이제야 좀 꿈인지 생시인지 분간이 가느냐?”

“어느 정도는요.”

처음 깨어났을 때와 똑같은 대답에, 적천강이 다시 주먹을 말아 쥐었다.

“지금은?”

“……와, 생시! 매우 생시! 온 세상이 아름답습니다! 살아 있는 게 너무 기뻐요!”

“좋아. 이제야 겨우 노부가 알던 천둥벌거숭이로 돌아왔구먼.”

“조금 전에는 아니었습니까?”

“몰라서 묻느냐? 천지 분간도 안 되는지 깨어나자마자 난동을 피우기에 모두 내보냈다.”

“음.”

생각해 보니 그랬던 것 같기도 하다.

너무나도 큰 혼란스러움에 몸부림치고, 붙잡으려는 손길들을 본능적으로 떨쳐 냈으니.

더군다나 부정할 수 없는 증거가 눈앞에 떡 하니 놓여 있었다.

“개판이네요.”

본래의 형체를 잃고 산산조각 난 파편들을 바라보며 중얼거리자, 적천강이 크게 고개를 끄덕여 동의를 표했다.

“아주 개판이지.”

“이것도 제가 한 겁니까?”

“반은 맞고, 반은 틀렸다.”

“그 말씀은…….”

“네 큰형 되는 놈이 난동을 피우더군. 덩치는 산만 한 것이 눈물까지 질질 짜면서 나갈 수 없다고 어찌나 버티던지. 별수 없이 노부가 직접 손을 썼다.”

나는 눈을 부릅뜬 채 적천강을 바라보았다.

“죽이셨습니까?”

“네 녀석부터 죽여 주랴?”

“아뇨. 농담입니다.”

“노부는 아니다.”

“오.”

한참 예전 같았다면 다이너마이트가 자동 장착된 똥줄을 붙잡고 카운트를 셌겠지만, 이제는 아니다.

아무런 대답 없이 피식 웃는 내 모습에, 적천강이 작게 혀를 찼다.

“염병할. 이제는 노부를 아주 개똥으로 아는구먼.”

“어허, 또 틱틱대신다. 다 아시면서.”

“알기는 개뿔이. 그보다…… 무엇 때문이냐?”

흐려지는 말꼬리에 덧붙여진 짤막한 물음.

나는 어느새 식은땀으로 축축해진 등골을 느끼며 입을 열었다.

“단순히 꿈 때문입니다.”

“대관절 어떤 악몽이었기에?”

“아뇨. 악몽이라기보다는……. 잘 모르겠어요. 뭐라 표현할 수 없는 이상한 꿈이어서.”

대답을 하면서도 느껴지는 묘한 기분에, 나는 문득 눈살을 찌푸렸다.

‘뭐지?’

왠지 모르게 낯익은 상황.

그러나 찰나 지간에 엄습해온 기시감은, 뒤이어 들려온 적천강의 심각한 목소리에 지워졌다.

“더 자세히 말해 보거라. 혹여 그 악몽이 네 안에 깃든 심마(心魔)의 흔적일 수도 있으니.”

잠깐의 망설임을 떨쳐낸 내가 대답했다.

“아마도 아닐 겁니다. 그건 그냥, 일종의 기억이었어요.”

“불행한 기억도 심마의 흔적이 될 수 있지. 노부 역시 그러한 과거에 사로잡혀 끝끝내 파멸을 맞이하는 자들을 보았던 적이 있다.”

적천강이 무엇을 우려하는지는 나 역시 알고 있다.

현대식으로 표현하자면, 일종의 트라우마라고나 할까.

무림인이 자신의 한계를 벗어나 지고한 경지에 다다르기 위해 필요한 것은 비단 강대한 공력과 무공뿐만이 아니다.

심상(心想)의 수련을 통해 얻는, 정신적인 깨달음.

그것이 선이든 악이든, 자신만의 깨달음을 얻어야만 그 길을 계속해서 걸어 나갈 자격을 얻을 수 있다.

그리고 이 과정에서 치유되지 못하고 얼룩진 마음의 병마는 심상의 수련하는 단계에 접어든 이들에게 있어 실로 치명적이다.

‘노야가 조필. 아니, 장천을 잃은 직후부터 노환을 앓았던 것처럼.’

그렇기에 적천강이 이렇게까지 심각하게 접근하는 것 역시 결코 과민반응은 아니었다.

세인들이 알고 있는 화왕 적천강은 겁화(劫火)나 다름없는 성미를 지녔지만, 그 내면에는 아득한 세월 동안 다듬어 온 신중함과 지혜가 숨겨져 있는 사람이니까.

하지만 이번만큼은, 그러한 적천강의 의견에도 망설임 없이 단언할 수 있었다.

“심마가 아닙니다.”

확신에 찬 한 마디에 얼굴을 굳힌 적천강을 응시하며, 나는 천천히 말을 이었다.

“꿈속에서 보았던 그 기억은, 애초에 제 것이 아니었으니까요.”

“네 것이 아니라니. 그게 무슨?”

나는 어느덧 파르르 떨리는 호흡을 삼켰다.

그리고, 동시에 떠올렸다.

한없이 몽롱했던 꿈속의 세상에서, 깊은 잠에 빠져드는 아이의 귓가에 흐릿하게 스며들었던 사내의 목소리를.

아니, 또 다른 아버지의 목소리를.



‘좋은 꿈 꾸거라. 우리 아들……. 태경아.’



그것은 내 기억인 동시에, ‘너’라 부를 수밖에 없는 누군가의 기억이었다.

태원진가의 삼공자 진태경.

가문의 수치이자, 이 몸의 본래 주인.
```

## Final English reading copy

```markdown
# Chapter 991

Whenever I lost consciousness or fell into a deep sleep, getting caught up in some kind of dream was nothing special anymore.

As someone once said, dreams were a window into the mind. Worries I hadn’t managed to shake off and memories that still lingered would get mixed and mashed together, then surface as the illusion we called a dream.

In the end, everything in this world had a cause or a reason. Dreams were no different.

Right.

That had to be true.

At least, as far as I knew.

But then why…

*Why am I having this dream?*

I slowly blinked in the blur of my vision.

Everything was hazy.

Unlike my other dreams, which had been horrifyingly vivid, I couldn’t even make out the illusions around me.

But when someone’s voice suddenly reached me, I finally understood the source of this haze.



*You look awfully sleepy, kid.*



Sleepy.

As the realization finally sank in, I lifted my head.

No—“my head was lifted” might be more accurate.

The eyes that had been blinking from the start, that movement of my head, and even the voice slipping between my lips now weren’t under my control.



*Yeah. I’m sleepy.*



The voice sounded muffled, as though I were underwater, but one thing was clear.

I was a child.

A child so young that hearing myself whine didn’t feel strange at all.

That answered one question, but a new one quickly took its place.

Who was the unfamiliar man whose voice was patiently indulging the child’s whining?

*I’ve never heard his voice before.*

A voice wasn’t exactly an ID card. I couldn’t be expected to recognize someone the instant I heard them. Still, anyone who showed up in my dreams ought to be familiar to me.

But everything seemed unfamiliar now.

The voice reaching me through my blurry vision. The illusion playing back in slow motion, like a TV screen full of static.

And when I heard the child’s words slip between lips that weren’t mine, I understood where this strange sense of unfamiliarity came from.



*Dad. Can I go to sleep?*



If I’d been able to speak of my own accord, I would’ve let out a groan without realizing it.

The truth I’d stumbled across was that astonishing—and that hard to understand.

*Dad?*

No. That couldn’t be.

I could turn over and shake out the oldest drawer of my memories, and still find no memory like this.

The voice of my father that remained in my mind, however faint, was nothing like the man’s voice coming through my hazy vision.

So this was—

*Not my memory.*

Just then, an inexplicable chill ran down my spine.

The unfamiliar man, the one the child had called Dad, spoke into my ear.



*Have a good dream, son.*



A warm hand stroked my hair. His voice was gentle.

As my vision plunged into darkness, the man’s final words rang faintly in my ears.



*…a.*



It was faint, but I’d heard it clearly.

A father’s voice speaking to his son. His son’s name.

And at that moment, my thoughts ground to a halt with the shock of something I’d never expected.

Fwoosh.

Light poured down from beyond the pitch-black darkness, wrapping around the child lost in deep sleep.

No—around me.



* * *



If someone asked what I saw first whenever I regained consciousness, I’d say the ceiling.

Or Hyuk Mujin, snoring in a corner of the room under the pretense of standing guard. Or Jeok Cheongang, who’d stayed by my side until I woke up.

But this time, it was none of those.

“Hah… hah…”

I shot upright like a spring and sucked in ragged breaths.

Was this what it felt like to be on the verge of suffocating?

The vision I’d only just regained wavered like melting candle wax, and the voices coming from all around me rang in my ears like thunder.

“Medicine King…! Come! Hurry!”

“…tain, Captain!”

“What the hell…!”

Was I still dreaming? Or was this real?

I couldn’t tell one from the other. Caught in confusion, I kept batting away the hands reaching for me on instinct.

Then someone grabbed me by the shoulder.

Firmly.

Even in the middle of all that, I could feel the strength in that hand with perfect clarity.

A faint pain came with it, along with an unfamiliar warmth.

Shaa…

My whole body, tense as a board, slowly relaxed.

Only then did I realize whose energy was flowing along the acupoint pathways known to just two people in this vast world—the Extreme Yang qi flowing through me.

“...Old Master.”

At the words I breathed out along with the breath I’d been holding, a voice I knew all too well answered me.

“Stay just as you are for a moment. Just a moment.”

I closed my eyes as Jeok Cheongang told me to.

I reminded myself that this place I was in was real, not an illusion, and slowly calmed my heart, which was pounding without pause.

How much time passed like that?

At last, I opened my eyes and faced a world that was both quiet and clear.

And a familiar face looking at me with concern.

“You fool. Are you finally coming around?”

I hesitated a moment before answering his blunt question.

“More or less.”

“So you’re not quite there yet.”

“Could you hit me hard once?”

“What?”

“Just once. Don’t hold back at all. Put your whole heart into it.”

“……”

“Please.”

At my solemn request, Jeok Cheongang sighed and raised his fist.

“Fine. You asked for it.”

Whoosh.

White flames sprang up in an instant, wrapping around his tightly clenched fist.

As I watched him prepare to fire off a move from the Flame-Extinguishing Divine Fist without another word, I calmly spoke up.

“Wow, that’s hot.”

“What kind of nonsense is that? The Fire Gate Clan’s martial arts have always been like that.”

“If I can feel how hot it is, I think I’ve definitely come to my senses.”

Jeok Cheongang shook his head.

“Doesn’t look like it to me.”

“I’ve changed my mind. I think I’m all right.”

“You said to put my whole heart into it.”

“Not quite that much.”

“Weren’t you the one who asked?”

“If you were going to take me that seriously, you should’ve refused three times first. Isn’t that just good manners?”

“You lunatic. Do you think I’m Zhuge Cheongang? Quit flapping that mouth and brace yourself.”

Despite his words, Jeok Cheongang lowered his fist. He flicked his hand, and a water bottle on the bedside table shot toward me.

“What are you waiting for? Drink something.”

“Thank you.”

I drained the full bottle in one go without stopping to breathe.

The cold water ran down my parched throat, and at last I felt like I could breathe again.

“Whew.”

“Well? Can you tell whether you’re dreaming or awake now?”

“More or less.”

At the same answer I’d given before, Jeok Cheongang clenched his fist again.

“And now?”

“...Whoa, I’m awake! Definitely awake! The whole world is beautiful! I’m so happy to be alive!”

“Good. You’re finally back to the reckless little brat I know.”

“Was I not a moment ago?”

“Do you really have to ask? You woke up and immediately started thrashing around like you couldn’t tell up from down, so I sent everyone else out.”

“Hmm.”

Now that I thought about it, that did sound familiar.

I’d been overwhelmed by confusion, fighting against the hands trying to hold me back.

And I had undeniable proof right there in front of me.

“What a mess.”

I muttered as I looked at the fragments scattered everywhere, their original forms lost. Jeok Cheongang nodded emphatically in agreement.

“It’s a hell of a mess.”

“Did I do this, too?”

“You’re half right and half wrong.”

“What do you mean…?”

“Your eldest brother was the one who made a scene. Built like a mountain, bawling his eyes out and insisting he couldn’t leave. I had no choice but to deal with him myself.”

I stared at Jeok Cheongang, eyes wide.

“Did you kill him?”

“Want me to kill you first?”

“No. I’m joking.”

“I’m not.”

“Oh.”

A long time ago, I would’ve been clutching my ass, which came equipped with a built-in stick of dynamite, and counting down. Not anymore.

I gave a quiet laugh without answering. Jeok Cheongang clicked his tongue.

“Damn it. Now you really do think I’m worth less than dirt.”

“Come on, you’re always snapping at me. You know I know better.”

“Know what, my ass. More importantly… what caused this?”

The question came with a brief pause, his voice trailing off.

I opened my mouth, feeling the sweat that had soaked my back.

“It was just a dream.”

“What sort of nightmare was it?”

“No, I wouldn’t call it a nightmare… I don’t know. It was a strange dream I can’t really describe.”

Even as I answered, an odd feeling crept over me. I frowned.

*What is this?*

The situation felt strangely familiar.

But the sense of déjà vu that had come over me vanished when Jeok Cheongang spoke again, his voice grave.

“Tell me more. That nightmare might have been a trace of the Heart Demon inside you.”

I pushed aside my brief hesitation and answered.

“I don’t think so. It was just a memory.”

“Even an unhappy memory can leave a trace of the Heart Demon. I’ve seen people who were trapped by such a past until it brought them to ruin.”

I knew what Jeok Cheongang was worried about.

In modern terms, it was something like trauma.

For a Murim martial artist to break past their limits and reach the highest realms, powerful internal energy and martial arts weren’t enough.

They needed spiritual insight gained through training the mind.

Whether good or evil, they had to gain an understanding of their own before they could keep walking that path.

And for anyone who’d begun that mental training, an illness of the heart left untreated could be devastating.

*Like how Old Master suffered from the infirmities of old age after losing Jopil. No—Jangcheon.*

That was why Jeok Cheongang’s serious concern wasn’t an overreaction at all.

People knew the Fire King Jeok Cheongang for a temper like hellfire, but beneath that burned the caution and wisdom he’d honed over a lifetime.

But this time, I could answer his concern without hesitation.

“It’s not the Heart Demon.”

I met Jeok Cheongang’s gaze as his expression hardened, then continued slowly.

“Because the memory I saw in the dream wasn’t mine to begin with.”

“What do you mean, it wasn’t yours?”

I swallowed a breath that had begun to tremble.

And at the same time, I remembered.

The man’s voice, faintly seeping into the ear of a child falling into a deep sleep in that hazy dream.

No—the voice of another father.



*Have a good dream, my son… Taekyung.*



It was my memory, and at the same time, the memory of someone I could only call *you*.

Jin Taekyung, Third Young Master of the Jin Family of Taiyuan.

The family’s disgrace, and the original owner of this body.
```
