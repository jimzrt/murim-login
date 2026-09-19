<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0495.txt",
      "sha256": "dbc6bcb8e4625134076bb7fcbe6af4a30e381b3b18b06392392c0d76a7ac6589",
      "bytes": 12838
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "9b52596ba560556282ef7cc2da24e608f25a92627723b5b2c922b0518d916934",
      "bytes": 4649
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "171bc34a2f45c3108d7fef999b92576366fd6e0179de1d6fcd883a4322b045a9",
      "bytes": 157784
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "e7c9ddadc703d3e2baa248436bbecdc50ce260d7f4c047b218b5f772c4412bd2",
      "bytes": 553
    },
    {
      "path": "characters/Hyeongong.md",
      "sha256": "2b43b70ea49cb2424de677d74abf05f8175106d3550be474afb4240a141b7f80",
      "bytes": 768
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "ca313758a5a3db926ba4d473fb13bf498475fe4b79f942adb69d92ab3ac04952",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "8eb8a75923791221bae99009919b305ef99d71f4f94b26d6adf515253e0e13eb",
      "bytes": 1547
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "fe9a7746993d8e5bcd09fd9eeecc29655f09869aee0f3f46bd5958c418ebcce7",
      "bytes": 1239
    },
    {
      "path": "characters/Luoyang Strange Physician.md",
      "sha256": "d07dd80f7e217b20d15e3b826ef14cf027ba125889ed3d19082c869ff8ff829e",
      "bytes": 855
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "3b3a2b5913bbba5ab8a1a13b7f47a9a82e53ea7f0e37f8d7ff54da82bc619542",
      "bytes": 885
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "fcd89ef22d5cd9bc5646cb7dfc2a01c58c5dc8bb04ac6b55736f44af7216f5ad",
      "bytes": 153645
    }
  ],
  "estimated_tokens": 11920
}
-->

# Durable State Update — Chapter 495

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 495. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 495. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 495,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 495,
    "continuity_sources": [495],
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
    "The functionally crippled Gate continues leaking faint mana; its residual mana is mutating local life, and the Water God Dragon absorbed all of that mana.",
    "Around one hundred Level 5 Mutated Minnows, locally called Blood Fish, have been captured in the Gate's entrance waterways; the remaining population is unknown, and the fish fight and kill one another.",
    "Taekyung suspects Dark Heaven's regeneration, teleportation, and Moving Formation are manifestations of Magic connected to the Gate.",
    "Taekyung told Jeok that he came from another world, that an evil force from it is linked to Dark Heaven, that the corrupted imugi was their work, and that a fully opened Gate could release monsters.",
    "Honglan corrupted the benevolent Dongting Lake imugi and used it to kill many people; the severely injured Dongting Fisherman may be connected to Dark Heaven and the earlier destruction inside the secret refuge.",
    "The Southern Heaven Demon Empress is traveling toward Yunnan and expects to cause further deaths.",
    "Jin Wikyung and Gung Gibang pledged the Jin Family of Taiyuan and the Beggars' Sect to Taekyung's defense.",
    "Jeok's innate qi is damaged and steadily diminishing despite the Thousand-Year Snow Ginseng and the Divine Physician's treatment, and he has withdrawn from the Water God Dragon expedition.",
    "Mungyeong is the Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history; before becoming the Slaughter Saint, he was called Killing Ghost, and he saved countless people as the Divine Physician.",
    "Mungyeong recognizes Taekyung's Heavenly Martial Physique as innate and distinct from Cheongpung's more refined physique.",
    "Mungyeong is testing Taekyung through successive poisoned traps and concealed attacks, intending to teach secret martial arts without a formal Master-Disciple relationship and to correct Taekyung's complacency.",
    "Taekyung detoxified Potent Seven-Step Soul-Chasing Powder, but Sinews and Meridians damage permanently reduced Strength and Agility by 5 each; the Water God Dragon's corpse is being dismantled under Taekyung's direction."
  ],
  "continuity_sources": [
    494,
    493
  ],
  "open_questions": [
    "What lies beyond the exposed Gate, why has it lost most of its functions, and how far has its residual mana's mutation spread?",
    "What is the Lord of Heaven's identity, and how is he connected to the dangerous force Taekyung associates with his original world?",
    "Where is the Southern Heaven Demon Empress ultimately headed, and what does she intend to do in Yunnan?",
    "What is the Dongting Fisherman's exact role within Dark Heaven, and how was he connected to the earlier destruction inside the secret refuge?",
    "What further poison tests will Mungyeong impose on Taekyung, and what secret martial arts will he teach him?"
  ],
  "safe_through": 494,
  "temporary_decisions": [
    "Render 산공독 as Energy-Dispersing Poison, 강력한 산공독 as Potent Energy-Dispersing Poison, 칠보추혼산 as Seven-Step Soul-Chasing Powder, 강력한 칠보추혼산 as Potent Seven-Step Soul-Chasing Powder, 심각한 복통 as Severe Stomachache, 고기 방패 as Meat Shield, 독 장아찌 as Poisoned Pickle, and 독의 as Poison Physician; retain secret martial arts, Master-Disciple relationship, Killing Ghost, and Fake Murim Martial Artist, and preserve 악 as Agh in the Quest interface.",
    "Render 기억의 파편 as Memory Fragment, 게이트 공략 as Gate Conquest, 텔레포트 as Teleport, 마법 as Magic, 혈어 as Blood Fish, and 변이된 송사리 as Mutated Minnow; render 강력한 마비산 as Potent Paralysis Powder, 강력한 미혼산 as Potent Soul-Bewitching Powder, 전신 마비 as Full-Body Paralysis, 독성 흡수 as Poison Absorption, and 해독 as Detoxification.",
    "Render 시산혈해 as sea of corpses and blood and retain Old Master for 노야 with the established rough, profane Taekyung-Jeok banter; render 해시 as hour of the Pig, 한 식경 as half an hour, 타구봉 as Dog-Beating Staff, 창룡 as Azure Dragon, and 무량수불 as Infinite Life Buddha.",
    "Render 선천지기 as innate qi, 진원진기 as true-origin qi, and 천기 as heavenly patterns.",
    "Render 심마 as Heart Demon, 비급 as martial arts manual, 송문고검 as Pine-Pattern Ancient Sword, 반로환동 as Returned to Youth, 강강수월래 as Ganggangsullae, 생사부 as Book of Life and Death, 기막 as qi curtain, 무극태을검 as Martial Extremity Grand Unity Sword, and 이룡 as Two Dragons."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 태원진가   | **Jin Family of Taiyuan**        |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 로그아웃             | **Logout**                     |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 노부      | **this old man / I**                                            |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 현공진인 | **Perfected Being Hyeongong** | Veteran Wudang Daoist master and the current Sect Leader's Junior Brother. |
| 낙양괴의 | **Luoyang Strange Physician** | Renowned Central Plains physician; eccentric and fiercely temperamental, he examined Jeok Cheongang. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 평화 | **Peace Guild** | Guild name. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 설삼 | **snow ginseng** | Elixir compared with the chapter's three selected roots. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 낙양 | **Luoyang** | Historic city in Henan Province and the chapter’s setting. |
| 신성 | **Morning Star** | Term in the summons referring to the Master of Morning Star. |
| 태극혜검 | **Taiji Wisdom Sword** | Wudang’s supreme sword technique. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 천년설삼 | **Thousand-Year Snow Ginseng** | Secret Zhongnan Sect cargo; a fully digested specimen can grant a full jiazi of internal energy. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 성도 | **Chengdu** | Sichuan destination of Taekyung's party. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 이무기 | **imugi** | Legendary serpent mentioned as the only comparable creature to a Thousand-Year Poison Horned Snake. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 골골 | **Golgoli** | Jin's nickname for the Skeleton King. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |
| 수신룡 | **Water God Dragon** | Legendary name for the true master of Dongting Lake; distinct from the modern Sea Serpent. |
| 원정 | **Origin Essence** | The Water God Dragon's purified energy core, which humans call an inner core. |
| 칠보추혼산 | **Seven-Step Soul-Chasing Powder** | Named extreme poison used in Mungyeong's training test. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 적천강 | 문경 | overwhelming elder to old acquaintance | you / little punk | mocking and threatening | Mocks Mungyeong's expression and threatens to poke out his eyes. |
| 적천강 | 수신룡 | legendary_martial_master_to_dying_spirit_beast | you | wary and trembling | Jeok asks what the Water God Dragon is after witnessing its mental communication. |
| 문경 | 수신룡 | physician_to_dying_spirit_beast | you | guarded and curious | Mungyeong asks whether the Water God Dragon knows him. |
| 진위경 | 현공진인 | Lesser Family Head to senior Wudang master | Perfected Being Hyeongong | formal-respectful | Addresses Hyeongong as 진인 while praising the Water God Dragon. |
| 문경 | 혁무진 | traveling_companion_to_traveling_companion | Martial Warrior Hyuk | formal-polite | Mungyeong asks Mujin to deliver water to Taekyung and lets Mujin receive the credit. |
| 혁무진 | 문경 | traveling_companion_to_traveling_companion | Mungyeong | casual-familiar | Mujin recognizes Mungyeong while reacting to Taekyung's dismantling work. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 494
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Hyeongong.md

# Perfected Being Hyeongong (현공진인)

- **Safe through:** Chapter 494
- **Aliases:** None
- **Role:** Perfected Being Hyeongong is a veteran Wudang Daoist master of the previous generation, the current Sect Leader's Junior Brother, and a Supreme Peak swordsman who reached the ultimate stage of the Taiji Wisdom Sword.
- **Personality:** Hyeongong is humble and self-deprecating about his limited worldly knowledge, carries the authority of an experienced senior master, and openly covets exceptional weapons.
- **Voice:** Measured, respectful, and lightly self-deprecating.
- **Relationships:** Hyeongong is the current Wudang Sect Leader's Junior Brother and a respected senior to Zhuge Feng.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 494
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 494
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin and Furnace Fire Pure Blue, and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 492
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Luoyang Strange Physician.md

# Luoyang Strange Physician (낙양괴의)

- **Safe through:** Chapter 341
- **Aliases:** None
- **Role:** Renowned physician of the Central Plains who comes to examine Jeok Cheongang at dawn in the Murim Alliance pavilion and is knocked unconscious with a concussion when Jin Taekyung’s thrown flower vase strikes him in the forehead; after waking one shichen later, he examines Jeok Cheongang, determines that Jeok’s qi acupoints will gradually become blocked and estimates six months at most, then directs Taekyung to seek the Divine Physician after providing a clue that the Divine Physician is in Sichuan.
- **Personality:** Eccentric and fiercely temperamental.
- **Voice:** Fierce and loud when angered.
- **Relationships:** Was sent by Mae Jonghak to examine Jeok Cheongang.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 494
- **Aliases:** Killing Ghost
- **Role:** Mungyeong is the legendary physician known as the former Divine Physician and Slaughter Saint, a Returned to Youth Supreme Peak master and the greatest assassin in history who passed the Divine Physician title to his Disciple.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, Jeok Cheongang is an old acquaintance who asked him to look after and instruct Jin Taekyung, and Mungyeong is currently testing Taekyung before teaching him secret martial arts without a formal Master-Disciple relationship.

## Korean source

```text
＃495화



갓난아이 시절에는 소변을 가리는 게 오히려 이상한 일이다.

일곱 살? 유치원생이니까 그럴 수 있다. 초등학생이라면 조금 부끄럽겠지만, 저학년일 경우에는 아주 없는 일도 아니었다.

하지만 내 나이는 스물일곱이다.

21세기 현대 매스컴은 앞다투어 나를 새로운 영웅이라 추앙하고, 천하의 무림인들은 화왕의 후인이자 향후 무림의 판도를 뒤바꿀 신성이라 부른다.

그런데, 그런데…….

‘씨벌.’

시원하게 싸질러 버렸다. 스물일곱에. 소변도 아니고 똥을. 그것도 문경이 보는 앞에서.



‘아, 아아. 아나스타샤!’

‘……천천히 닦고 와라.’



한참이나 침묵하던 문경은 그 한 마디를 남기고 떠나 버렸다.

내가 안쓰러워서라기보다는 혹여나 자신의 소검에 똥이 묻을까 걱정되는 기색이 역력했다. 염병할 늙은이 같으니라고.

조금 전의 일을 떠올릴 때마다 암천이고 나발이고 로그아웃해서 두 번 다시 돌아오기 싫어진다.

‘이참에 아예 무림을 뜰까.’

물가에 앉아 진지하게 고민하고 있던 내게, 한 사람이 웃음기 띤 얼굴로 다가왔다.

“조장님. 거기서 혼자 뭐 하십…….”

익숙한 얼굴을 발견한 나는 진심을 담아 쌍욕을 날렸다.

“혁무진, 이 개새끼야.”

“아니, 갑자기 왜 욕을 하세요?”

“넌 한동안 내 눈에 띄지 마라. 제발.”

“아무리 조장님이어도 그렇지. 웃는 사람 얼굴에 침 뱉기 있습니까?”

“카악, 퉤!”

“어억!”

아슬아슬하게 가래침을 피해 낸 혁무진이 정신병자를 바라보는 듯한 시선으로 나를 훑었다.

“무슨 일이길래 이러십니까?”

“아무 일도 없었어. 그러니까 제발 입 다물고 내 눈앞에서 사라져.”

“뭔가 문맥이 이상한데요.”

“팔다리 위치를 이상하게 만들어 줄까?”

저놈이 가져다준 물 때문에 능력치도 잃고, 인간으로서의 존엄성도 잃었다.

진짜 원흉이 문경이라는 걸 알기에 주먹이 나가려는 것을 가까스로 참고 있는 거다.

그런 속사정을 모르는 혁무진은 황당한 표정이었다.

“거 참. 누가 보면 꼭 저 때문에 바지에 똥이라도 지린 줄 알겠네요.”

“……!”

“뭡니까, 지금 그 반응은?”

“……아무것도 아냐. 그런데 왜 왔어?”

미심쩍은 눈빛으로 나를 바라보던 혁무진이 저 멀리 떨어진 사람들을 가리켰다.

“대강 분류가 끝났는데, 좀 이상하다고 해서요.”

“이상해? 뭐가?”

“이무기의 뼈와 비늘의 양이 생각보다 적은 모양입니다. 조장님께서 직접 가 보셔야 할 것 같은데요.”

“그래?”

“예. 이무기의 덩치에 비해 나온 너무 양이 적다고, 지금 진노하신 현공진인께서 주위를 이 잡듯 뒤지고 있어요. 만약 누군가 훔친 거라면 원시천존의 명예를 걸고 범인을 밝혀 내시겠답니다.”

“…….”

아니, 자기가 무당탐정 김전일이야 뭐야.

본인은 뼈 좀 얻겠다고 태극혜검까지 써 가며 도왔는데, 누군가 낼름 가져갔다고 생각하니 꼭지가 돌아 버린 모양이다.

듣다 보니 어이가 없어진 내가 혁무진을 향해 물었다.

“아니, 그걸 어떻게 슬쩍해? 그리고 사라진 양이 적은 것도 아니고 족히 천 근은 넘을 텐데. 어느 누가 우리 눈을 피해서 숨긴다고.”

“그렇죠. 애초에 이 장소를 아는 사람도 극소수…….”

말을 이으려던 혁무진이 멈칫하더니 되물었다.

“그런데 어떻게 아셨어요?”

“응?”

“없어진 양이요. 천 근은 넘을 거라고 하셨잖아요.”

“그냥 대충 넘겨짚은 거지, 뭐. 아까부터 저쪽에서 워낙 시끄럽기도 했고.”

최대한 담담하게 대답했지만, 순간 뜨끔했다.

왜냐하면…….

‘눈치 빠른 놈. 말조심해야겠네.’

현공진인이 원시천존의 명예를 걸고 찾아내겠다고 한 범인이 바로 나니까.

인벤토리에 가득 쌓인 부산물을 생각할 때마다 절로 배가 부를 지경이다.

‘음. 그러고 보니 많이 챙기긴 했지.’

그건 누워서 스마트폰 만지는 것보다 쉬운 일이었다.

수신룡의 사체는 워낙 거대했고, 나는 누구보다 많은 부분을 손질하면서 알짜라고 부를 만한 부위를 인벤토리에 쓸어 담았다.

가장 날카로운 꼬리뼈, 유난히 단단했던 목 부위의 비늘, 혹시 몰라서 챙긴 살점까지.

그렇게 빼돌린 걸 전부 한 자리에 쌓아 놓는다면 어지간한 장원도 찜 쪄 먹을 만한 크기일 거다.

“……왜 그렇게 흐뭇하게 웃으세요?”

“내가? 내가 언제?”

“방금요. 되게 음흉해 보이셨는데.”

아무래도 완전 범죄에 성공했다는 기쁨이 얼굴에 고스란히 드러난 모양이다. 나는 정색하며 대답했다.

“그런 적 없는데?”

“…….”

“어쨌건 저쪽 일은 신경 쓰지 말고, 가서 슬슬 준비나 해라.”

“무슨 준비요?”

“돌아가야지. 여기서 평생 살래?”

이미 분류된 수신룡의 사체는 믿을 만한 사람들에 의해 아주 은밀히, 조금씩 옮겨질 것이다.

그리고 그중 대부분은 태원진가의 몫이 되겠지.

‘앞으로 벌어질 전투를 생각하면 큰 힘이 될 거야.’

생각을 정리한 나는 자리에서 일어났다.

이미 내 말이 떨어지기 무섭게 저 멀리 달려가고 있는 혁무진의 뒷모습을 바라보다, 마음속으로 읊조렸다.

‘인벤토리 오픈, 소환.’

스슥.

시동어와 동시에 손에 잡히는 수신룡의 뼈와 비늘. 그리고 살점. 절로 흐뭇한 미소가 지어진다.

‘아이템 감정.’

띠링.



아이템창



[수신룡의 뼈]

종류 : 재료

등급 : 초절정

제한 : 명장(名匠)만이 제련 가능

설명 : 장구한 세월을 살아온 이무기, 수신룡의 뼈. 대단한 강도를 지녔으며 정체 모를 영험한 기운이 깃들어 있다. 경지에 이른 장인의 손을 거친다면 진정한 힘을 끌어낼 수 있을 것.





비록 약간의 차이는 있지만, 비늘에 대한 시스템 창의 설명도 비슷했다.

영험한 기운이 깃들어 있으며 엄청난 강도를 지닌 초절정의 재료라는 것이 요지였고, 살점의 경우에는 장복(長服)할 경우 공력과 능력치를 올릴 수 있다고 했다.

‘이 정도면 복권 당첨된 거지.’

하지만 진짜 복권은 따로 있었다.

뼈와 비늘이 로또요, 살점이 연금복권이라면 이건 당첨금의 사이즈가 다른 아메리카 슈퍼볼이다.

나는 두근거리는 마음으로 ‘그것’을 인벤토리에서 꺼내 들었다.

‘아이템 감정.’

띠링.



아이템창



[수신룡의 원정]

종류 : 無

등급 : 無

제한 : 無

설명 : 장구한 세월을 살아온 이무기, 수신룡의 원정(元淨). 마력에 의해 손상되었으나 수신룡의 의지에 따라 추출된 내단의 일종이다. 지극히 정순하면서도 막대한 기운을 품고 있으며, 일반적인 영약과는 궤를 달리한다. 다만 원정에 담긴 기운을 견디지 못한다면…… 이하 생략.





‘끝내준다.’

나는 손에 든 [수신룡의 원정]을 조심스럽게 어루만졌다.

마지막 줄이 의미심장하긴 해도, 이것이야말로 이번 호북행에서 얻은 가장 큰 수확이다.

‘일반적인 영약과는 궤를 달리한다…… 그럼 어느 정도인 거지?’

마력에 오염되었던 탓에 수신룡이 원래 가지고 있던 기운의 크기보다는 못하겠지만, 그래도 엄청난 것은 매한가지다.

수신룡은 무려 오백여 년을 살았고, 그건 단순 계산으로도 최소 십 갑자 이상의 기운을 쌓았다는 뜻이다.

그런 의미에서 보자면 원정의 힘이 줄어든 것은 오히려 전화위복(轉禍爲福)이나 다름없다.

‘그릇이 작으면 물이 흘러넘치는 법.’

아이템 설명의 마지막 줄이 알려 주듯이, 아무리 나라고 해도 그 정도의 기운을 한 번에 받아들였다가는 풍선처럼 터져 버리고 말 테니까.

‘문제는 이걸 언제, 어디에 쓰냐인데.’

머릿속에 떠오르는 몇 사람의 면면. 그중 유독 늙은 한 사람의 얼굴이 자꾸만 눈앞에 아른거린다.

‘노야.’

적천강을 떠올린 것은 단순히 그가 늙었기 때문만은 아니었다.

그 이유는 우습게도 문경의 독 때문이다.

칠보추혼산의 후유증으로 피 같은 능력치가 10포인트가 깎여 나가고, 심각한 복통으로 똥을 지리고 나니 뇌리에 스치는 생각이 있었다.

‘칠보추혼산이 이 정도인데. 무형지독(無形至毒)에 당한 노야는 어떤 상태일까.’

칠보추혼산은 분명 극독이지만, 경지에 오른 초절정 고수의 목숨을 위협할 만큼은 아니다.

하지만 적천강이 하남에서 중독되었던 무형지독은 칠보추혼산 따위는 비교도 되지 않을 만큼 엄청난 독성을 품고 있었다.

천하에서 손꼽히는 명의인 낙양괴의조차 해답을 찾지 못해 신의를 찾아보라 권했을 정도였고, 그마저도 독성이 많이 퍼진 탓에 만독지환을 구해야 했다.

‘다행히 천년설삼(千年雪蔘)이 있어 치료를 끝내긴 했지만…….’

정말 별다른 후유증 없이 완치된 걸까.

나는 의문과 걱정이 뒤섞인 눈빛으로 [수신룡의 원정]을 응시했다.

어쩌면 이건, 처음부터 쓰임새가 정해져 있던 물건일지도 모르겠다.

“막내야!”

인벤토리 오픈. 수납.

등 뒤에서 들려온 진위경의 외침에 재빨리 [수신룡의 원정]을 인벤토리에 집어넣은 나는 애써 웃으며 돌아섰다.

“네, 지금 갑니다!”

오늘은 여러 가지 만족스러운 수확을 얻은 날이다.

하지만 그럼에도 불구하고 마음 한구석이 무거운 날이었고, 어쩐지 모르게 뱃속이 뒤틀리는 듯한 날이기도 했다.

꾸루루루룩.

“……후.”

아, 상태 이상 아직 안 풀렸구나.



* * *



물을 찾아 정착하는 것은 사람만이 갖는 습성이 아니었다. 자연 속의 동물도 마찬가지다.

너른 동정호의 강물을 따라 늘어선 절벽에 둥지를 튼 새들을 시작으로 멧돼지, 여우, 늑대. 그리고 호랑이까지.

절벽 아래의 동정호가 인간에게 허락된 구역이라면, 절벽 위는 동물들의 것이었다.

사람의 발길이 닿지 않은 평화로운 공간.

그렇기에 이곳의 왕이라 할 수 있는 대호(大虎)는 갑작스럽게 찾아온 불청객이 마뜩잖았다.

- 크르르르릉.

날카로운 이빨 사이로 흘러나오는 울음소리에 불편한 심기가 고스란히 묻어 나온다.

쉴새 없이 벌름거리는 코는 아직도 사라지지 않은 인간의 냄새를 쫓고 있었다.

그리고 민감한 후각이 목표를 찾기까지는, 그리 오랜 시간이 걸리지 않았다.

- 크릉.

깎아내린 듯한 절벽의 끄트머리. 초대받지 않은 불청객을 발견한 대호는 코웃음 쳤다.

어느 간 큰 놈인가 했더니, 불청객은 대호가 생각했던 것 이상으로 작고 초라했다.

한 입 거리도 되지 않을 것 같은 늙은 인간이 바로 불청객의 정체였다.

스으윽.

수백 근에 달하는 몸뚱어리가 늙은 인간을 향해 기민하게 다가가던 바로 그 순간이었다.

“범이 있었군.”

- ……!

소리 죽여 다가가던 대호의 발걸음이 멈칫했다.

어느새 짤막한 다리로 자리에서 일어난 늙은 인간이 대호를 빤히 바라보고 있었다.

“늙은 녀석이로구나. 너도.”

- 크르릉.

대호는 보란 듯이 이빨을 드러냈지만 늙은 인간은 피식 실소를 흘릴 뿐이었다.

“소란피우지 말고 이리 오거라. 노부의 말벗이나 해다오.”

- 크와아아앙!

“이 줄 그어진 개새끼가 뒈질라고. 이리 오라니까.”

흠칫!

어째서일까. 대호는 전신의 털이 바짝 솟구치는 것을 느끼며 엉거주춤 늙은 인간을 향해 다가갔다.

주름진 손이 턱을 살살 긁자, 자신도 모르게 기분이 좋아졌다.

- 그르르릉.

골골거리는 대호의 모습을 바라보던 늙은 인간, 화왕 적천강은 작게 중얼거렸다.

“그래, 이미 늙어 버렸어.”

절벽 위로 펼쳐진 하늘은 맑았고, 그의 마음은 어두웠다.
```

## Final English reading copy

```markdown
# Chapter 495

When you’re a newborn, not being able to control your bladder is perfectly normal.

At seven? If you’re kindergarten age, it happens. If you’re in elementary school, it would be a little embarrassing, but it’s not unheard of in the lower grades.

But I was twenty-seven.

The twenty-first-century mass media had competed to proclaim me a new hero, while the martial artists of Murim called me the heir of the Fire King and a rising star destined to change the face of Murim.

And yet…

*Fuck.*

I had taken a huge dump. At twenty-seven. Not just peed myself, either. I had shit myself. In front of Mungyeong, no less.

*Ah, ahh. Anastasia!*

*……Take your time cleaning up and come back.*

After a long silence, Mungyeong left me with only those words.

It was obvious that he was less worried about me than about getting shit on his short sword. What a damn old man.

Every time I thought about what had just happened, I wanted to log out and never return to Murim again. To hell with Dark Heaven and everything else.

*Should I just leave Murim altogether?*

As I sat by the water, seriously contemplating it, someone approached me with a smile on his face.

“Captain. What are you doing all by your—”

The moment I saw the familiar face, I unleashed a heartfelt string of profanity.

“Hyuk Mujin, you son of a bitch.”

“Why are you swearing at me all of a sudden?”

“Stay out of my sight for a while. Please.”

“Even if you’re the Captain, that’s too much. Is that any way to spit in a smiling person’s face?”

“Khack—ptui!”

“Gah!”

Hyuk Mujin barely dodged the glob of phlegm and looked me over as though I were a lunatic.

“What happened to make you act like this?”

“Nothing happened. So shut up and disappear from in front of me.”

“Something about that context seems off.”

“Want me to rearrange your arms and legs?”

Because of the water that bastard had brought me, I had lost stats and my dignity as a human being.

I was barely holding back my fist because I knew Mungyeong was the real culprit.

Hyuk Mujin, unaware of the circumstances, looked bewildered.

“Good grief. Anyone watching would think you’d shit your pants because of me.”

“……!”

“What is that reaction supposed to mean?”

“……Nothing. Why are you here?”

Hyuk Mujin watched me suspiciously, then pointed toward the people standing in the distance.

“We’ve mostly finished sorting things, but apparently there’s something strange.”

“Strange? What?”

“It seems there are fewer bones and scales from the imugi than expected. I think you should come take a look yourself.”

“Really?”

“Yes. He’s furious because the amount recovered is far too little compared to the imugi’s size. He’s searching the area as though he’s hunting lice. He says that if someone stole it, he’ll uncover the culprit in the name of the Primordial Heavenly Venerable’s honor.”

“……”

What was he, Detective Kindaichi?

He must have completely lost his mind after helping with the Taiji Wisdom Sword just to obtain some bones, only to think someone had snatched them away.

The more I listened, the more absurd it seemed, so I asked Hyuk Mujin,

“How could anyone steal it? And it’s not like only a little went missing. It must be well over a thousand geun.[^1] How could anyone hide that without us noticing?”

“Exactly. Besides, only a handful of people even know this place—”

Hyuk Mujin stopped mid-sentence and turned to me.

“But how did you know?”

“Hm?”

“About the amount that disappeared. You said it must be over a thousand geun.”

“I just took a rough guess. They’ve been making an awful racket over there for a while.”

I answered as calmly as I could, but I felt a sudden stab of guilt.

Because…

*He’s sharp. I need to watch what I say.*

The culprit Perfected Being Hyeongong had sworn to find was me.

Every time I thought about all the by-products piled up in my inventory, I felt full.

*Come to think of it, I did take quite a lot.*

It had been easier than lying in bed playing with my smartphone.

The Water God Dragon’s corpse was enormous, and I had personally worked on more of it than anyone else, sweeping all the choice pieces into my inventory.

The sharpest tailbone, the unusually hard scales from its neck, and even some flesh I had taken just in case.

If I piled everything I had smuggled away in one place, it would be large enough to dwarf a decent-sized manor.

“……Why are you smiling so contentedly?”

“Me? When did I?”

“Just now. You looked incredibly shady.”

Apparently, the joy of having pulled off the perfect crime had shown plainly on my face. I answered with a straight face.

“I didn’t do that.”

“…….”

“Anyway, don’t worry about what’s happening over there. Go get things ready.”

“Ready for what?”

“We’re going back. Do you want to live here forever?”

The Water God Dragon’s already sorted corpse would be moved little by little, very discreetly, by people we could trust.

Most of it would become the property of the Jin Family of Taiyuan.

*It’ll be a huge help when the battles ahead begin.*

After organizing my thoughts, I stood up.

Hyuk Mujin had already run off into the distance the moment I finished speaking. Watching his retreating back, I muttered inwardly.

*Inventory open. Summon.*

Shhk.

As soon as I spoke the activation words, the Water God Dragon’s bones, scales, and flesh appeared in my hands. A satisfied smile spread across my face.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Water God Dragon’s Bones**
>
> **Type:** Material  
> **Grade:** Supreme Peak  
> **Restriction:** Only a Master Artisan can forge it.
>
> **Description:** The bones of the imugi known as the Water God Dragon, who lived for countless years. They possess incredible hardness and contain an unknown sacred energy. If worked by a Master Artisan who has reached the proper realm, their true power can be drawn out.

Although there were slight differences, the System’s description of the scales was similar.

The gist was that they were Supreme Peak materials containing sacred energy and possessing incredible hardness. As for the flesh, it said that consuming it over a long period could increase internal energy and abilities.

*This is like winning the lottery.*

But the real lottery prize was something else entirely.

If the bones and scales were Lotto and the flesh an annuity lottery, this was the American Powerball, with a jackpot on an entirely different scale.

With my heart pounding, I took *it* out of my inventory.

*Item appraisal.*

Ding.

> **System**
>
> **Item Window**
>
> **Water God Dragon’s Origin Essence**
>
> **Type:** None  
> **Grade:** None  
> **Restriction:** None
>
> **Description:** The Origin Essence of the imugi known as the Water God Dragon, who lived for countless years. Though damaged by mana, it is a type of inner core extracted according to the Water God Dragon’s will. It contains qi that is exceptionally pure and immense, and is on an entirely different level from ordinary elixirs. However, if you cannot withstand the qi contained within it… (The rest is omitted.)

*Amazing.*

I carefully stroked the **Water God Dragon’s Origin Essence** in my hand.

The final line was ominous, but this was undoubtedly the greatest reward I had gained from my trip to Hubei.

*“On an entirely different level from ordinary elixirs.” How powerful could it be?*

It had been contaminated by mana, so it was probably inferior to the amount of qi the Water God Dragon had originally possessed. Even so, it was still immense.

The Water God Dragon had lived for more than five hundred years. Even by a simple calculation, that meant it had accumulated at least ten jiazi of qi.

From that perspective, the reduction in the Origin Essence’s power was practically a blessing in disguise.

*When the vessel is small, the water spills over.*

As the final line of the item description suggested, even I would burst like a balloon if I tried to take in that much qi all at once.

*The question is when and where to use it.*

The faces of several people appeared in my mind. One particularly old face kept floating before my eyes.

*Old Master.*

I had not thought of Jeok Cheongang merely because he was old.

The reason, absurdly enough, was Mungyeong’s poison.

After losing ten points of my precious stats to the aftereffects of Seven-Step Soul-Chasing Powder and then shitting myself because of the Severe Stomachache, a thought had crossed my mind.

*If Seven-Step Soul-Chasing Powder did this much… What condition must Old Master be in after being poisoned by the Formless Ultimate Poison?*

Seven-Step Soul-Chasing Powder was certainly an extreme poison, but it was not powerful enough to threaten the life of a Supreme Peak master who had reached a proper realm.

The Formless Ultimate Poison that had infected Jeok Cheongang in Henan, however, contained a level of toxicity that made Seven-Step Soul-Chasing Powder look insignificant.

Even the Luoyang Strange Physician, one of the most renowned physicians in the world, had failed to find an answer and advised us to seek the Divine Physician. And because the poison had already spread so extensively, we had needed to obtain the Myriad-Poison Ring.

*Fortunately, the treatment was completed thanks to the Thousand-Year Snow Ginseng…*

But had he really recovered without any significant aftereffects?

I stared at the **Water God Dragon’s Origin Essence**, my gaze filled with both doubt and worry.

Perhaps this was an item whose purpose had been decided from the very beginning.

“Little Brother!”

*Inventory open. Store.*

I hurriedly put the **Water God Dragon’s Origin Essence** back into my inventory at Jin Wikyung’s shout from behind me, then turned around with an awkward smile.

“Yes, I’m coming!”

Today had been a day of many satisfying gains.

And yet it was also a day when one corner of my heart felt heavy, and when my stomach seemed to twist for some reason.

Grrrggg.

“……Sigh.”

Ah. The status abnormality still hadn’t worn off.

* * *

Settling near water was not a habit unique to humans. Animals in nature did the same.

Birds nesting along the cliffs that lined the broad waters of Dongting Lake, followed by wild boars, foxes, wolves—and even tigers.

If Dongting Lake below the cliffs was territory permitted to humans, then the cliffs above belonged to the animals.

It was a peaceful place where no human foot had ever reached.

That was why the great tiger, the king of this place, was displeased by the sudden arrival of an uninvited guest.

- Grrrrrrr.

The growl spilling between its sharp teeth carried all its irritation.

Its nose flared without pause as it tracked the human scent that had yet to fade.

It did not take long for its sensitive sense of smell to locate its target.

- Grrr.

At the edge of a cliff that dropped away as though it had been carved straight down, the great tiger discovered the uninvited guest and snorted.

What kind of audacious fool had come here? As it turned out, the visitor was even smaller and shabbier than the tiger had expected.

The uninvited guest was an old human who did not even look large enough for one bite.

Ssshhk.

The moment the body weighing several hundred geun moved nimbly toward the old man, the old man spoke.

“So there was a tiger.”

- ……!

The great tiger’s silent approach came to an abrupt halt.

The old man, who had risen to his feet on his short legs, was staring straight at it.

“You’re an old one too.”

- Grrr.

The great tiger bared its teeth, but the old man merely let out a quiet laugh.

“Don’t make such a fuss. Come here and keep this old man company.”

- Raaaargh!

“You striped mutt, do you want to die? I said come here.”

The great tiger flinched.

For some reason, it felt every hair on its body stand on end as it awkwardly approached the old man.

When the wrinkled hand gently scratched its chin, it felt good despite itself.

- Prrrrr.

Watching the great tiger purr, the old man—Fire King Jeok Cheongang—murmured softly.

“Yes. I’ve already grown old.”

The sky spread above the cliffs was clear, but his heart was dark.

[^1]: A geun is a traditional East Asian unit of weight; a Korean geun is roughly 600 grams.
```
