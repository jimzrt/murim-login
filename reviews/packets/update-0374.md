<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0374.txt",
      "sha256": "9797fdbcdc38bec11b446c08086192cd8372fee85866f8a37126956e49661da4",
      "bytes": 14370
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "6e0243c6462767071f326acfeb91cf088ad56d57f50e3e7ff5a2e51a34b46304",
      "bytes": 2613
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "35a64b0ee8e102918af3654d7e7dcd31b09e2733a5228bdd3a3a0b3e9ed1e3ba",
      "bytes": 130340
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "d2266fff5d839082d115a738a0c5da983fe52fddc6693f02d777fc642af2b669",
      "bytes": 570
    },
    {
      "path": "characters/Heaven-Shaking Venerable Nun.md",
      "sha256": "eb4de5ff1f8f9f8c0ee8f33815c4a14d35dc331d1a79860c46337b1bbcbe5be8",
      "bytes": 510
    },
    {
      "path": "characters/Hwangso.md",
      "sha256": "4f9b79c38f6a785832b23baf4a4e14c44cb646b5b7a3ccac8dcb660a05036c2f",
      "bytes": 698
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "cf09bb409a398b1c9c19c96a240c3ad8311ce6b1352f843b407d8592ebe0a3c4",
      "bytes": 1345
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "f37447a042c909929fe33ccd7f56309a0b9f89bfa3ce5bd2b34d55a2b8a9d532",
      "bytes": 1477
    },
    {
      "path": "characters/Tang Sadok.md",
      "sha256": "0dd03423ca1f75fd22c3870a60e5882f48471e7de32ca9a6fd2f8b6f958dd5bc",
      "bytes": 771
    },
    {
      "path": "characters/Western Heaven Demon Lord.md",
      "sha256": "05a0c003d4575c791601ae80a15963076f8709cd74d73d5429be25d069ac3790",
      "bytes": 888
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "7ef8282657f7c47c8ab92e32779d8e5232d53cbb2519bfea13564906b90d6e9c",
      "bytes": 99419
    }
  ],
  "estimated_tokens": 11700
}
-->

# Durable State Update — Chapter 374

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 374. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 374. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings (Arabic digits allowed in titles such as 1팀장; do not romanize). At
least one endpoint must occur in the source. The controller drops pairs already
in the address ledger. Do not invent risk-register rows. Beat plot paragraphs
are plain strings; continuity and translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 374,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 374,
    "continuity_sources": [374],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "The Sichuan Tang Clan is rebuilding seven days after the Three-Gate Bloodbath, which caused catastrophic casualties and ongoing funerals.",
    "Most Dark Heaven attackers involved in the Sichuan assault are dead or captured; Mungyeong captured the Third Fiend in the hidden cavern, while the Second Fiend's fate is unknown.",
    "Jin Taekyung is awake, has reached Level 120 and the Supreme Peak realm, manifested Force, and is publicly known as the Blazing Flame Divine Dragon.",
    "Jeok Cheongang is alive but remains weakened and is recovering his strength.",
    "Dong Feng's dantian and martial arts were destroyed while shielding Jeok Cheongang; the Divine Physician is Mungyeong's Master.",
    "Mungyeong is the Slaughter Saint and Dong Feng's Disciple; he has sworn never to kill again and intends to live as a medical apprentice.",
    "Hyuk Mujin and Gung Gibang remain badly wounded after fighting the Third Fiend.",
    "Cheongpung remains a Supreme Peak master at the Sichuan Tang Clan with Mimi.",
    "The Lord of Heaven temporarily possessed the Western Heaven Demon Lord's body and escaped after One Annihilation.",
    "The Myriad-Poison Ring remains in Jin Taekyung's possession and cannot be appraised by the System.",
    "A hidden cavern near Chengdu contains the inactive Moving Formation used by Dark Heaven; the Slaughter Saint identifies Dark Heaven as the successor to the Demonic Cult.",
    "The second bound Item in Jin's inventory remains unnamed, and an investigation team from Henan has arrived seeking him."
  ],
  "continuity_sources": [
    373
  ],
  "open_questions": [
    "What happened to the Second Fiend assigned to the Qingcheng attack?",
    "Why did Mungyeong tell the companions that Jin Taekyung ordered the rescue of Emei?",
    "What is the true nature and purpose of the Lord of Heaven, and what became of the Western Heaven Demon Lord?",
    "What was the origin and purpose of the Moving Formation, and why did it lose its power?",
    "How will Dark Heaven respond to the failed Three-Gate Bloodbath?"
  ],
  "safe_through": 373,
  "temporary_decisions": [
    "Render 열화신룡 as Blazing Flame Divine Dragon, distinct from Huashan Divine Dragon.",
    "Use Mimi for 미미 and Mimi-chan for 미미쨩.",
    "Use Third Fiend for singular 삼괴 references and Three Fiends for collective references.",
    "Render 진인 as Perfected One, 도우 as Fellow Daoist, and 신니 as Venerable Nun in forms of address.",
    "Render 환영진 as illusion formation and 이동진 as Moving Formation."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 매종학    | **Mae Jonghak**    |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 독왕     | **Poison King**               | Tang Taesang   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 소림     | **Shaolin**                      |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 무인     | **martial artist**                               | Default term                                          |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 전음     | **Sound Transmission**                           | Fixed skill terminology; preserve the internal-energy mechanism when the source explains it, but do not add an explanation where it does not |
| 정파     | **orthodox faction**                             |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 경천신니 | **Heaven-Shaking Venerable Nun** | Former Emei Sect Leader and sole Supreme Peak master; killed on Mount Emei. |
| 황소 | **Hwangso** | First-generation disciple of the Gongdao Sect and a reluctant search-party member. |
| 당사독 | **Tang Sadok** | Current Family Head of the Sichuan Tang Clan; also called the Myriad-Poison Asura. |
| 서천마군 | **Western Heaven Demon Lord** | Title of the middle-aged antagonist who commands the summoned black-robed hunters. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 사자후 | **lion's roar** | Taekyung's term for Song Il's crowd-shattering roar. |
| 사천당문 | **Sichuan Tang Clan** | Martial clan cited for its poison-based cleansing method. |
| 아마존 | **Amazon** | Region referenced in Taekyung's crude joke. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 당문 | **Tang Clan** | Short form for the Sichuan Tang Clan. |
| 아미 | **Emei** | Short form for Emei Sect. |
| 아미파 | **Emei Sect** | Murim sect in Sichuan. |
| 청성 | **Qingcheng** | Short form for Qingcheng Sect. |
| 소림혈사 | **Shaolin Bloodshed** | Past incident cited by Hwangbo Eom. |
| 만독수라 | **Myriad-Poison Asura** | Epithet of Tang Sadok. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 삼괴 | **Three Fiends** | Collective form used by the Western Heaven Demon Lord for the Qilian Three Fiends. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 마군 | **Demon Lord** | Shortened title used for the Western Heaven Demon Lord. |
| 삼문혈사 | **Three-Gate Bloodbath** | Name given to Dark Heaven’s coordinated assault on the Tang Clan, Qingcheng, and Emei. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 서천마군 | 당사독 | hostile_opponents | you | calm and taunting | The Western Heaven Demon Lord uses 자네 while answering Tang Sadok's question. |
| 당사독 | 서천마군 | hostile_opponents | you bastard | hostile and threatening | Tang Sadok uses 네놈 after recognizing the disguised infiltrator. |
| 서천마군 | 신의 | hostile_invader_to_physician | Divine Physician | calm and mocking | Uses 신의 and 그대 while taunting the physician and dismissing his objections. |
| 신의 | 서천마군 | physician_to_invading_fiend | fiend | defiant and formal | Calls the Western Heaven Demon Lord an 악귀 and orders him to leave. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 373
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is the legendary physician also known as Dong Feng and Mungyeong's Master, whose dantian and martial arts were destroyed while shielding Jeok Cheongang.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** The Slaughter Saint is his Master, and Mungyeong is his Disciple.

### Heaven-Shaking Venerable Nun.md

# Heaven-Shaking Venerable Nun (경천신니)

- **Safe through:** Chapter 371
- **Aliases:** Blood Rakshasa
- **Role:** Former Emei Sect Leader and the sect's sole Supreme Peak master, killed on Mount Emei by a one-armed middle-aged man.
- **Personality:** Forthright and fearless against enemies.
- **Voice:** Not established.
- **Relationships:** Respected leader of the Emei Sect; she and three Emei Elders were killed in the same attack.

### Hwangso.md

# Hwangso (황소)

- **Safe through:** Chapter 369
- **Aliases:** None
- **Role:** First-generation disciple of the Gongdao Sect in Sichuan, deployed with roughly thirty second- and third-generation disciples to search for the surviving Third Fiend.
- **Personality:** Privileged, impatient, pleasure-seeking, inattentive, and dismissive of the danger surrounding the mission.
- **Voice:** Complaining and casual, with irreverent sarcasm toward his Senior Brother and the search.
- **Relationships:** His Senior Brother supervises him, and his prosperous merchant father forced him into the Murim to establish family connections.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 360
- **Aliases:** Junzi Sword
- **Role:** Thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan. He has led the family in place of the absent Family Head and established it as Shanxi Murim's hegemon. He is a senior commander of the Jin Family and its wartime alliances, and investigates threats to the family and Shanxi.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 355
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Tang Sadok.md

# Tang Sadok (당사독)

- **Safe through:** Chapter 371
- **Aliases:** Myriad-Poison Asura
- **Role:** Current Family Head of the Sichuan Tang Clan, gravely wounded after being forced to watch the clan’s destruction but still alive and receiving treatment from Cheongpung.
- **Personality:** Grim, cold, blunt, suspicious, and unsentimental, with fierce concern for the Tang Clan’s affairs.
- **Voice:** Hissing, curt, authoritative, and threatening.
- **Relationships:** Tang Taesang was his father and predecessor as Family Head, his unnamed nephew serves as Master of the Gatekeeper Pavilion, and the Thousand-Year Poison Horned Snake was his father's final gift and is his cherished companion.

### Western Heaven Demon Lord.md

# Western Heaven Demon Lord (서천마군)

- **Safe through:** Chapter 372
- **Aliases:** None
- **Role:** Former Protector of the Divine Cult who commands Dark Heaven's assault on the Sichuan Tang Clan, lost the Myriad-Poison Ring to Jin Taekyung, suffered a crushed ankle and a torn wrist, and was temporarily possessed by the Lord of Heaven before the borrowed body was destroyed.
- **Personality:** Cold, detached, patient, and utterly ruthless toward those he interrogates or hunts.
- **Voice:** Controlled and dispassionate, with concise statements delivered in a quiet, threatening tone.
- **Relationships:** Tang Taesang and the Heaven-Shaking Venerable Nun were his latest victims, he lost one arm taking their lives, and the Qilian Three Fiends now submit to him alongside his hundreds of black-robed hunters.

## Korean source

```text
＃374화



독룡각(毒龍閣)의 각주인 당호룡은 자리에서 일어나 손님을 맞이했다.

지금 막 문을 열고 들어온 장대한 체구의 사내에게서는 알 수 없는 위압감이 흘러넘쳤다.

“먼 길 오느라 노고 많으셨소.”

“사천당문이 겪은 고초에 비하면 아무것도 아니지요. 다시 한번 심심한 유감을 표합니다.”

거친 용모와는 달리 사내의 목소리는 낮고 부드러웠으며, 동시에 듣는 이로 하여금 집중하게 만드는 힘이 있었다.

무리를 이끄는 지도자만이 가지는 기세라고 할까? 온화하면서도 깊게 가라앉은 사내의 눈빛에, 당호룡은 문득 한 사람을 떠올렸다.

‘이건…… 또 다른 종형(從兄)과 마주한 느낌이로군.’

그 사실은 당호룡을 적잖이 당혹스럽게 했다.

듣기로 눈앞의 사내는 불혹도 채 되지 않은 젊은 나이라고 했다.

반면 그의 종형은 연배는 물론이거니와 무림에서의 입지도 대단한 인물이었다.

정마대전이라는 전란 속에서 숱한 전공을 쌓고, 무너졌던 가문을 더욱 단단하게 일으켜 세운 철혈의 가주이기도 했다.

만독수라(萬毒修羅) 당사독.

사천당문의 가주 대행, 당호룡은 아직도 의식을 회복하지 못한 자신의 종형을 떠올리며 내심 한숨을 내쉬었다.

‘어서 일어나서 우리를 이끌어 주십시오. 가주.’

당호룡은 천생 무인이었다.

독과 암기에 관해서는 일가를 이루었다고 자부하는 그였지만, 가문을 이끄는 것은 또 다른 영역이었다.

특히 최근에는 곳곳에서 밀려드는 온갖 사안들에 혈육을 잃은 슬픔과 분노를 떠올릴 틈조차 없을 정도였다.

‘차라리 이런 자가 지금 내 자리에 있었다면 좋았을 것을.’

그런 의미에서 당호룡은 눈앞의 사내가 못내 부러웠다.

단순히 첫인상만을 가지고 판단하는 것이 아니라, 사내에 관한 소문을 익히 들었기 때문이었다.

그 소문의 반의반만 사실이라 해도 사내는 능히 일가를 이끌 역량의 소유자였다.

“당 대협. 혹시 제 얼굴에 뭐라도 묻었습니까?”

“아, 아무것도 아니오. 워낙 경황이 없어 무례를 범했구려.”

당호룡의 황급한 사과에 사내가 진중한 얼굴로 고개를 끄덕였다.

“아닙니다. 그럴 만도 하지요. 그토록 참담한 일을 겪으셨으니.”

사실 이번에 사천당문이 입은 피해는 참담이라는 말로도 부족했다.

구 할에 달하는 식솔들이 유명을 달리했고, 사천당문의 경내 대부분이 파괴되었으니까.

가문의 명맥을 보존했다는 것이 그나마 위안이었지만, 과거의 성세를 회복하기 위해서는 아주 오랜 시간이 필요할 터였다.

“사천 무림의 동도들이 발 벗고 나서 도와주고는 있으나…… 앞으로의 일이 우려되는구려.”

가주인 당사독이라면 어떤 상황에서도 약한 모습을 보이지 않았을 것이나, 당호룡은 달랐다.

그의 솔직한 말에 사내는 긴 손가락으로 찻잔을 어루만졌다.

“제가 이곳에 온 이유는 당 대협께서도 잘 아시리라 생각합니다.”

“삼문혈사를 조사하기 위해 온 것으로 알고 있소만.”

“정확히 말하자면, 처음 하남을 떠났을 때는 작고하신 독왕 당사독 대협과 경천신니를 시해한 흉수를 색출하기 위함이었습니다. 하지만 오는 길에 상황이 크게 바뀌었지요.”

“맞소. 암천, 그 천인공노할 놈들이 마수를 드러냈소.”

“비록 하남에서의 전례가 있기는 하나 이토록 대담하게, 그것도 천하에 명성이 자자한 세 곳의 명문 대파를 일거에 습격했다는 것은 전란이 코앞까지 들이닥쳤다는 증거입니다.”

작은 혼란은 더 큰 혼란을 낳는다.

그러나 암천의 존재는 이미 숨길 수 있는 수준의 것이 아니었고, 숨길 이유도 없었다.

참혹했던 삼문혈사의 그날로부터 어언 칠 주야.

지금쯤 발 없는 말은 천리를 달리고, 무수히 많은 전서구가 천하 각지로 날아가고 있을 것이다.

그리고 혼란이 아닌 전란은, 결집을 낳았다.

“소림혈사 직후 하남에서 정파 무림이 결집하고 있다 들었소. 그럼 혹시…….”

“아직은 준비 과정일 뿐입니다. 하지만 기정사실이지요.”

사내가 묵직한 음성으로 말을 이었다.

“그런 연유로 드리는 말씀인데, 하남으로 가시는 것이 어떻겠습니까.”

“하남이라.”

“예. 곧 생각하시는 그 일이 일어날 겁니다.”

짧은 침묵 끝에 당호룡이 입을 뗐다.

“영광스러운 자리에 초청해 준 것은 감사하나, 지금은 내가 자리를 비울 수 없소. 그대도 알다시피 가주 대행으로서 본가의 식솔들을…….”

“당 대협.”

“말씀하시오.”

“방금 말씀하신 것처럼 당 대협께서는 가주 대행이십니다. 당연히 당문의 식솔들을 놔두고 가실 수 없겠지요.”

“……!”

그제야 사내의 제안에 담긴 뜻을 알아차린 당호룡이 입을 벌렸다.

그로서는 감히 생각도 해 본 적 없는 일이었다.

“그러니까 지금…… 본가를 옮기라는 말이오?”

“글쎄요.”

사람의 속을 훤히 들여다보는 듯한 사내의 투명한 눈빛이 당호룡을 향했다.

“매종학 대협께서 제게 그런 말씀을 하시더군요. 곧 정마대전보다 더 거대한 전란이 발발할 것이라고.”

“검성께서…….”

당호룡은 침음성을 삼켰다.

저것은 비단 검성 한 사람만의 의견이 아닐 것이다.

지난 소림혈사는 수많은 정파 무림인들의 분노와 경각심을 일깨웠고, 새로운 무림맹(武林盟)은 이미 태동의 준비를 끝마쳤다.

정파 무림 전체가 곧 닥칠 전란에 대비하는 것이다.

‘이런 상황에서 본가가 살아남을 수 있을까.’

순간 뇌리를 스친 의문에 그의 가슴이 덜컥 내려앉았다.

이미 사천당문은 가문 역사상 유례없는 타격을 입었다.

더욱이 청성파와 아미파 역시 만만치 않은 전력을 잃은 상황.

다시 한번 적들이 쳐들어온다면 막을 방법은 요원했다.

“허어.”

망연자실한 얼굴로 한숨을 내쉬는 당호룡의 귓가에 나직한 목소리가 닿았다.

“당 대협께서는 사천당문이 지난 수백 년간 이어질 수 있었던 이유가 뭐라 생각하십니까.”

“그것은.”

“오직 당문(唐門)이었기 때문입니다. 앞의 두 글자를 떼어 낸다 한들 그 사실은 변하지 않습니다.”

“……!”

“결심하신다면, 정파 무림이 당문을 돕겠습니다.”

말을 잇지 못하고 파르르 몸을 떨던 당호룡이 어렵게 입을 열었다.

“우리는 지금껏 수많은 적을 만들었소. 구파일방과 오대세가에도 본가를 불편하게 생각하는 이들이 있지. 아무 문제 없겠소?”

“모든 일은 공명정대(公明正大)하게 이루어질 터. 안심하시고 새로운 둥지를 트십시오. 하남, 섬서, 아니면…….”

사내의 입가에 부드러운 웃음이 맺혔다.

“산서도 좋겠군요.”

“산서?”

“제게 말씀만 하십시오. 남는 땅 많습니다.”

당호룡은 문득 잊고 있던 사실 한 가지를 떠올렸다.

바로 눈앞의 사내가 산서 무림을 일통한 맹주이며, 산서성 제일의 지주이자 대부호라는 사실을.

“고맙소. 정말 고맙소, 진 대협!”

“별말씀을.”

사내, 태원진가의 소가주 진위경이 공손하게, 그러나 위엄 있는 태도로 사천당문 가주 대행의 포권에 답한 그 순간이었다.

덜컥.

“저기, 부르셨다고 들었는데요.”

전각의 문틈 사이로 빼꼼 고개를 내민 한 청년을 발견한 진위경이 사자후를 내질렀다.

“막내야아-!”

두두두두두, 퍼억!

흡사 성난 황소와도 같은 돌진이었다.

포옹인지 격돌인지 모를 두 형제의 상봉을 목격한 당호룡은 진위경에 관한 소문 중 하나를 떠올렸다.

‘아우들이라면 껌뻑 죽는다더니.’

산서 무림을 일통한 맹주이자 산서성 제일의 지주는 온데간데없고, 웬 팔불출 하나만 남아 있었다.

‘역시 아직 나이가 젊다 보니 연륜이 부족해. 언제 어디서나 냉철하신 종형에 비할 바가 아니지. 암, 그렇고말고.’

미미쨩의 존재를 알 리 없는 당호룡이었다.



* * *



“막내야아!”

축축한 눈물을 흩뿌리며 돌진한 진위경이 나를 덥석 끌어안았다.

이래 봬도 무림 짬밥 2년. 지금까지 지긋지긋하게 당한 일이라 이 정도 반응은 충분히 예상했다.

콰드득!

……그런데 이걸 예상 못 했네.

아니, 이게 뭐라고 뼈 어긋나는 소리가 들리냐. 나는 아마존 밀림의 아나콘다처럼 전신을 꽉꽉 조여 오는 포옹에 한숨을 내쉬었다.

어쨌거나 반가운 마음에 순순히 안겨 주긴 했는데, 반응이 역대 최고로 격렬했다.

“잠깐, 형님. 이것 좀 놓고 얘기합시다, 놓고.”

“형님이라니! 그런 딱딱한 호칭 말고 편하게 형이라고 부르라 하지 않았더냐! 변했구나, 변했어!”

“아, 알겠으니까 이제 좀 놔 봐요.”

“어릴 때는 반말하더니 존댓말은 왜 쓰는 것이냐! 변했구나, 변했어!”

“놔, 시벌.”

“헉, 아무리 삐뚤어졌을 때도 욕은 안 했는데! 변했구……!”

“와, 추임새 돌겠네.”

혹시 본업이 무림인이고 부업이 디멘터신가.

영혼이 빨려 나가는 듯한 기분에 진저리를 치며 손을 뻗었다.

휘릭, 쿵!

진위경의 거구가 거꾸로 땅에 처박히자 육중한 소리가 울려 퍼졌다.

지켜보던 사천당문의 장년 사내가 헉, 하고 신음을 흘렸다.

“괜찮습니다, 괜찮아요. 이거 그냥 저희끼리 노는 거예요.”

“아, 아니 그래도…….”

“보세요. 멀쩡히 일어나잖아요.”

내 말처럼 아무렇지 않게 벌떡 일어난 진위경은 감격의 눈물을 글썽이고 있었다.

“그사이 더 강해졌구나. 역시 우리 막내다.”

그 변함없는 모습에 나는 피식 실소를 흘렸다.

“참, 여전하네요.”

“여전하기는. 지난 두 달 동안 얼마나 걱정을 했는지 아느냐? 밤에 잠도 못 이루고 입맛도 없어서 피골이 상접했다.”

나는 우람한 근육질의 덩치를 보며 중얼거렸다.

“피골이 풍족해 보이는데.”

그나저나 두 달이라, 벌써 그렇게 시간이 흘렀구나.

나는 새삼 돌아갈 때가 임박했음을 깨달았다.

어느 한쪽의 세상에 열흘을 머무른다 쳤을 때 다른 한쪽에서는 한 시간 남짓이 소모되는 걸 감안한다면…….

‘얼추 여섯 시간 정도가 흘렀군. 슬슬 비행기가 착륙할지도 모르겠어.’

때마침 잘됐다. 서천마군이라는 큰 산을 넘으며 피로가 쌓인 차였으니까.

나는 말 길게 할 것 없이 대뜸 본론을 들이밀었다.

“언제 출발합니까?”

“우리 막내, 얼마나 고초가 컸을…… 응?”

안절부절못하며 내 몸을 살피던 진위경이 멈칫했다.

“지금 뭐라고?”

“저 데려가려고 오신 거잖아요. 아, 삼괴도.”

진위경의 눈이 휘둥그레졌다.

“그걸 네가 어떻게?”

사천당문의 중요 인물로 보이는 장년 사내도 놀란 얼굴로 입을 열었다.

“진 대협. 일의 전말에 대해 조사하러 오신 것이 아니었소?”

“맞습니다만, 조사단 중 저를 포함한 몇몇은 다시 하남으로 복귀할 겁니다. 사천에 도착하기 직전, 삼문혈사를 일으킨 주범 중 하나인 삼괴를 호송하라는 임무를 받았습니다.”

“그럼 본가에 관한 이야기는…….”

“물론 유효합니다. 단, 지금 당장은 당문으로서도 힘들겠지요.”

“그렇소. 가주께서도 아직 먼 거리를 이동할 수 없는 상황이니 말이오. 다른 식솔들에게도 동의를 구해야 하고.”

“예. 그리고…….”

잠시 장년인과 두런두런 이야기를 나누던 진위경이 내게 은밀히 전음을 날려 보냈다.

- 한데, 어찌 알고 있었더냐?

- 척 하면 착이죠. 그냥 정황상 이럴 것 같았어요.

- 아아, 우리 막내. 얼마나 큰 고비를 넘겼길래 머리까지 좋아졌단 말이냐!

- …….

뭔가 기분 나쁘네.

사실 정황상 알아차린 것도 아니다. 삼괴 호송 관련한 퀘스트가 떠서 안 거지.

“그래서 언제 출발합니까?”

내 물음에 막 대화를 끝마친 진위경이 입을 열었다.

“알고 있었다니 이야기가 쉽겠구나. 빠르면 빠를수록 좋다. 준비는 되었느냐?”

“어차피 가져온 거라고는 불알 두 짝밖에 없는데요. 몸만 가면 됩니다.”

거기에 더해 붕대를 칭칭 감은 짐 덩이 둘까지.

고개를 끄덕인 진위경이 입을 열었다.

“당 대협. 삼괴는 어디 있습니까?”

당 대협이라 불린 장년 사내가 대답했다.

“사지를 결박하고 철저한 감시 속에 가둬 두었소. 불알을 터트린 후로 틈만 나면 자결하려고 하니 주의해야 할 거요.”

“……저런.”

저건 나 같아도 죽고 싶을 것 같은데.

어찌 되었건 신속하게 움직일 수 있는 여건은 갖춰졌다.

잠시 무언가를 생각하던 진위경이 시원하게 대답했다.

“그렇다면 반 시진. 반 시진 안에 출발하는 것으로 하지. 괜찮으냐?”

“문제없습니다.”

망설임 없이 대답한 그 순간, 전각 밖에서 다급한 인기척과 함께 누군가의 외침이 들렸다.

“가주께서! 가주님께서 깨어나셨습니다!”

진위경이 미지근한 목소리로 말을 정정했다.

“한 시진. 한 시진으로 하자.”

“……예. 그게 좋겠네요.”

아깝다. 만독지환 먹튀 할 수 있었는데.
```

## Final English reading copy

```markdown
# Chapter 374

Tang Horyong, the Master of Poison Dragon Pavilion, rose from his seat to greet his guest.

An imposing man had just opened the door and entered, and an indescribable pressure radiated from him.

“You’ve worked hard coming all this way.”

“Compared to what the Sichuan Tang Clan has endured, it was nothing. Let me once again express my deepest condolences.”

Despite his rough features, the man’s voice was low and gentle. At the same time, it possessed a force that compelled listeners to pay attention.

*The aura possessed only by a leader who commands others, perhaps?*

The man’s eyes were gentle yet deeply settled, and they suddenly reminded Tang Horyong of someone.

*This feels like facing another older cousin…*

That realization left Tang Horyong more than a little flustered.

He had heard that the man before him was still young—not yet forty.

His older cousin, on the other hand, was an extraordinary figure not only in age but also in his standing within the Murim.

He was also an iron-willed Family Head who had accomplished countless military feats during the Great Faction War and rebuilt his fallen family stronger than ever.

Tang Sadok, the Myriad-Poison Asura.

Tang Horyong, the Acting Family Head of the Sichuan Tang Clan, inwardly sighed as he thought of his older cousin, who still had not regained consciousness.

*Please wake up soon and lead us, Family Head.*

Tang Horyong had been born a martial artist.

He prided himself on having mastered the use of poison and hidden weapons, but leading a family was an entirely different matter.

Especially lately, countless problems had been pouring in from every direction, leaving him no time even to think about the grief and anger caused by the loss of his blood relatives.

*It would have been nice if someone like this had been in my position instead.*

In that sense, Tang Horyong couldn’t help envying the man before him.

He wasn’t judging him solely by his first impression. He had already heard plenty of rumors about the man.

Even if only a quarter of those rumors were true, the man clearly possessed the ability to lead a family.

“Sir Tang, is there something on my face?”

“Ah, no. I was so distracted that I committed a discourtesy. My apologies.”

At Tang Horyong’s hurried apology, the man nodded with a solemn expression.

“Not at all. It’s understandable. You’ve suffered something so devastating.”

In truth, even the word *devastating* was insufficient to describe the damage suffered by the Sichuan Tang Clan.

Nearly ninety percent of the clan’s people had died, and most of the Tang Clan’s grounds had been destroyed.

The fact that the family line had survived was their only consolation. It would take an extraordinarily long time to restore the clan to its former glory.

“The fellow martial artists of Sichuan have been stepping forward to help us, but… I’m worried about what comes next.”

If Tang Sadok, the Family Head, had been in his position, he would never have shown weakness under any circumstances.

Tang Horyong was different.

At his honest words, the man gently ran his long fingers over his teacup.

“I believe you know why I came here, Sir Tang.”

“I understand that you came to investigate the Three-Gate Bloodbath.”

“To be precise, when I first left Henan, my purpose was to find the culprit who murdered the late Poison King Tang Sadok and the Heaven-Shaking Venerable Nun. However, the situation changed drastically on the way here.”

“That’s right. Dark Heaven, those bastards beyond the pale, finally revealed their fangs.”

“Although there was a precedent in Henan, the fact that they so boldly attacked three famous and powerful clans and sects known throughout the land all at once is proof that war has reached our doorstep.”

Small disturbances give birth to greater disturbances.

But Dark Heaven’s existence could no longer be concealed, nor was there any reason to hide it.

Seven days and seven nights had passed since the horrific day of the Three-Gate Bloodbath.

By now, word of mouth would be racing a thousand miles, and countless messenger pigeons would be flying to every corner of the realm.

And war, rather than mere chaos, had brought people together.

“I heard that the orthodox Murim of Henan is rallying in the aftermath of the Shaolin Bloodshed. In that case, perhaps…”

“For now, it is only in the preparation stages. But it is a foregone conclusion.”

The man continued in a weighty voice.

“That is why I ask: would you consider going to Henan?”

“Henan.”

“Yes. The thing you’re thinking of is going to happen soon.”

After a brief silence, Tang Horyong spoke.

“I’m grateful that you invited us to such an honorable occasion, but I cannot leave at present. As you know, as the Acting Family Head, the members of our family…”

“Sir Tang.”

“Please, go on.”

“As you just said, you are the Acting Family Head. Naturally, you cannot leave the members of the Tang Clan behind.”

“…”

Only then did Tang Horyong understand the meaning behind the man’s proposal. His mouth fell open.

It was something he had never dared even consider.

“So you’re saying that we should move our family headquarters?”

“Well…”

The man’s clear eyes, as if they could see straight through a person, turned toward Tang Horyong.

“Great Hero Mae Jonghak told me something. He said that a war even greater than the Great Faction War would soon break out.”

“The Sword Saint…”

Tang Horyong swallowed a groan.

That could not be the opinion of the Sword Saint alone.

The Shaolin Bloodshed had awakened the anger and vigilance of countless orthodox martial artists, and the new Murim Alliance had already finished preparing to emerge.

The entirety of the orthodox Murim was preparing for the war that would soon arrive.

*Can our family survive in a situation like this?*

The question flashed through his mind, and his heart sank.

The Sichuan Tang Clan had already suffered the greatest blow in its history.

Moreover, the Qingcheng Sect and Emei Sect had also lost considerable strength.

If the enemy invaded once more, they would have little hope of stopping them.

“Good heavens.”

As Tang Horyong sighed with a dazed expression, a quiet voice reached his ears.

“Sir Tang, why do you think the Sichuan Tang Clan has survived for the past several hundred years?”

“That is because…”

“Because it was the Tang Clan. Even if you strip away the name “Sichuan,” that fact does not change.”

“…”

“If you make up your mind, the orthodox Murim will help the Tang Clan.”

Tang Horyong trembled and struggled to open his mouth.

“We have made countless enemies over the years. Even among the Nine Sects and One Gang and the Five Great Families, there are those who harbor ill feelings toward our family. Will there truly be no problems?”

“Everything will be handled fairly and openly. Rest assured and build a new nest. Henan, Shaanxi, or…”

A gentle smile formed at the corners of the man’s mouth.

“Shanxi would be good as well.”

“Shanxi?”

“Just say the word. I have plenty of land to spare.”

Tang Horyong suddenly remembered one fact he had forgotten.

The man standing before him was the Alliance Leader who had unified Shanxi Murim, as well as Shanxi Province’s greatest landowner and wealthiest magnate.

“Thank you. Truly, thank you, Great Hero Jin!”

“It was nothing.”

At that moment, the man—Jin Wikyung, the Lesser Family Head of the Jin Family of Taiyuan—responded to the Acting Family Head of the Sichuan Tang Clan’s clasped-fist salute with a courteous yet dignified bearing.

Clunk.

“Um, I heard you called for me.”

Jin Wikyung spotted a young man poking his head through the gap in the pavilion door and let out a lion’s roar.

“My youngest!”

Thud-thud-thud-thud—crash!

His charge resembled that of an enraged bull.

As Tang Horyong watched the reunion of the two brothers, which was impossible to distinguish from either an embrace or a collision, one of the rumors he had heard about Jin Wikyung came to mind.

*They say he’s completely helpless when it comes to his younger brothers.*

The Alliance Leader who had unified Shanxi Murim and the greatest landowner in Shanxi Province was nowhere to be seen.

In his place stood nothing but a hopelessly doting fool.

*He’s still young, so he lacks experience. He can’t compare to my older cousin, who remains so clearheaded at all times and in all places. Yes, that’s right.*

Tang Horyong had no idea that Mimi-chan existed.

* * *

“My youngest!”

Jin Wikyung charged toward me, scattering tears from his damp eyes, and grabbed me in a fierce embrace.

I had been in the Murim for two years now. I had suffered through this kind of thing more times than I could count, so I had expected a reaction like this.

Crack!

…But I hadn’t expected that.

No, what was this supposed to be? Why did I hear bones shifting?

I sighed as he squeezed my entire body like an anaconda in the Amazon jungle.

Still, since he was happy to see me, I let him hug me without resisting.

But his reaction was more violent than ever before.

“Wait, Hyung-nim. Let’s talk after you let go. Let go.”

“Hyung-nim? Why are you using such a stiff form of address? Didn’t I tell you to call me hyung comfortably? You’ve changed. You’ve really changed!”

“Ah, all right, I get it, so let me go now.”

“You used to speak informally when you were little. Why are you using honorifics now? You’ve changed. You’ve really changed!”

“Let go, goddammit.”

“Gasp! You never swore, even when you were at your most rebellious! You’ve changed…”

“Wow, your running commentary is driving me crazy.”

Was his main job really being a martial artist, with being a Dementor as his side job?

Feeling as though my soul were being sucked out, I shuddered and stretched out my hand.

Whoosh—crash!

Jin Wikyung’s huge body was driven headfirst into the ground, and a heavy thud rang out.

A middle-aged man from the Sichuan Tang Clan, who had been watching us, let out a startled groan.

“It’s all right. It’s fine. We’re just playing around.”

“N-No, but…”

“Look. He’s getting right back up.”

Just as I had said, Jin Wikyung sprang to his feet as if nothing had happened, tears of emotion welling in his eyes.

“You’ve grown even stronger in the meantime. That’s my youngest.”

At his unchanged behavior, I let out a quiet laugh.

“You really haven’t changed.”

“Haven’t changed? Do you know how worried I’ve been these past two months? I couldn’t sleep at night, and I lost my appetite so badly that I became skin and bones.”

I looked over his enormous, muscular frame and muttered,

“Your skin and bones look awfully well-padded.”

Come to think of it, two months.

So much time had already passed.

I belatedly realized that it was almost time for me to return.

If ten days in one world amounted to roughly an hour passing in the other…

*About six hours must have passed. The plane might be landing soon.*

The timing couldn’t have been better. I had accumulated quite a bit of fatigue after getting over the mountain that was the Western Heaven Demon Lord.

Without bothering to say anything more, I got straight to the point.

“When are we leaving?”

“My youngest, you must have suffered so much… Hm?”

Jin Wikyung, who had been anxiously looking me over, stopped.

“What did you just say?”

“You came to take me with you, didn’t you? Ah, and the Third Fiend, too.”

Jin Wikyung’s eyes widened.

“How did you know that?”

The middle-aged man, who appeared to be an important figure in the Sichuan Tang Clan, also spoke with a surprised expression.

“Great Hero Jin, didn’t you come to investigate the whole matter?”

“I did, but some of us, myself included, will be returning to Henan. Just before we arrived in Sichuan, we received an assignment to escort the Third Fiend, one of the principal culprits behind the Three-Gate Bloodbath.”

“Then what about the matter concerning our family?”

“That offer remains valid, of course. But the Tang Clan will have difficulty moving right away.”

“That is true. The Family Head still cannot travel any great distance. We also need to obtain the consent of the other family members.”

“Yes. And…”

After quietly discussing something with the middle-aged man, Jin Wikyung sent me a covert Sound Transmission.

*How did you know?*

*You say it, I get it. The circumstances made it seem likely.*

*Ah, my youngest. What kind of ordeal did you go through to make you smarter as well?*

*…*

Something about that rubbed me the wrong way.

I hadn’t figured it out from the circumstances. I knew because a Quest concerning the Third Fiend’s escort had appeared.

“So when are we leaving?”

Jin Wikyung had just finished his conversation and answered my question.

“If you already knew, this will be easier. The sooner, the better. Are you ready?”

“The only things I brought with me were my two balls. I just need to leave with my body.”

Plus two bundles wrapped tightly in bandages.

Jin Wikyung nodded and turned to the middle-aged man.

“Sir Tang, where is the Third Fiend?”

The middle-aged man addressed as Sir Tang answered.

“We have him bound hand and foot and confined under close watch. Ever since his testicles were crushed, he’s been trying to kill himself whenever he gets the chance, so you’ll need to be careful.”

“…How awful.”

Even I would want to die after that.

In any case, we were ready to move quickly.

Jin Wikyung thought for a moment before answering decisively.

“Then half a shichen.[^1] We’ll leave within half a shichen. Is that acceptable?”

“No problem.”

The instant I answered without hesitation, a frantic commotion arose outside the pavilion, followed by someone shouting.

“The Family Head! The Family Head has awakened!”

Jin Wikyung amended his words in a lukewarm voice.

“One shichen. Let’s make it one shichen.”

“…Yes. That sounds better.”

What a shame. I could’ve taken the Myriad-Poison Ring and run.

[^1]: A shichen is a traditional Chinese time unit of roughly two hours.
```
