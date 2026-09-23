<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0868.txt",
      "sha256": "5c5e2f397fb5dffb343bc58b581e527979f6798e424e15eed81644de652dffa9",
      "bytes": 12978
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "0eb02e3f1fb04bae20b326e472830c41ab575d03c972ed0392e595f8b8468d94",
      "bytes": 2246
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "c6aa7ac66627729312c888562b57669d8c199736b3a54a323fd416b739461b8d",
      "bytes": 229550
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "7b4f7d4efe0833bd87bce9d21e5ccfc2034dcf86b6dffce8f5eaef686915ce91",
      "bytes": 811
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "9085360faf76713d6fdfa749331dc5eba8c82470bffb262d3fc353fe2ca87a9e",
      "bytes": 1378
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "d4cb80476d544f4829392ac18d527f8407a2accd1596abcc1759d7aef4bde420",
      "bytes": 1511
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "5136c541e8d942b6d3a8385f912dcf33788c73fd87d4966be7984923bf1f7c7a",
      "bytes": 1782
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "cba1a9b0ad62b131d34f70e2abd8299a18e0a79719b2b83ec3ebcf4582bdc47d",
      "bytes": 622
    },
    {
      "path": "characters/Ma Sanbao.md",
      "sha256": "1792f7bfac89babde9ccea2588ea1d11dfdfd1d4dfe807143005434255e88ab3",
      "bytes": 731
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "325742976b73247cac894421d289d3d936a2e8fafb8c8663baab8683aff8e29e",
      "bytes": 920
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a8141ce654787037f0430ec4bd957cdee026a5e328c854706643cba086a917a7",
      "bytes": 256358
    }
  ],
  "estimated_tokens": 11345
}
-->

# Durable State Update — Chapter 868

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
1 and safe_through 868. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 868. Profile updates may replace only one
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
  "chapter": 868,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 868,
    "continuity_sources": [868],
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
    "Prince Shangshan and his party remain inside the imperial palace under surveillance; the Emperor has scheduled Shangshan's audience for tomorrow.",
    "Baek Yeon helped the fourth prince seize the throne, betrayed the late Emperor and Crown Prince, and led a purge in which 30,000 people were arrested and killed.",
    "Hong Jin is devoted to protecting Shangshan and trusts Jin Taekyung to help keep him safe.",
    "Ma Sanbao, the East Depot's second-in-command, has secretly remained in the palace loyal to the late Emperor and is ready to act against the current ruler.",
    "Ma Sanbao and Hong Jin are longtime friends and allies; Ma's intelligence about disguised Embroidered Uniform Guard members heading toward Shanxi helped Hong prepare before seeking Taekyung's aid.",
    "An unidentified assassin reached Qianqing Palace, concealed poison beneath a molar, and died by suicide before capture; the assassin's identity and backer are unknown.",
    "The Emperor and Baek Yeon share an old promise tied to a great undertaking; Baek urges the Emperor to restore things to their proper place before their adversaries' moves unravel them.",
    "The Emperor relies on opium, which he calls medicine, and breaks his pipe to clear his mind."
  ],
  "continuity_sources": [
    866,
    867
  ],
  "open_questions": [
    "What action do Ma Sanbao and Hong Jin intend to take against the current ruler, and when?",
    "What does the Emperor intend for Prince Shangshan, and why was his audience postponed?",
    "Who sent the assassin to Qianqing Palace, and what was the intended target?",
    "What was the old promise between Baek Yeon and the Emperor, and what does Baek mean by restoring things to their proper place?",
    "What happened between Hong Jin and the old eunuch, and why did Hong Jin leave the East Depot?"
  ],
  "safe_through": 867,
  "temporary_decisions": [
    "Render 동창 병필태감 as “Brush-Holding Eunuch of the East Depot.”",
    "Render 첩형 as “Constable” and 태감 as “Eunuch” in forms of address.",
    "Render 앵속 as “opium” and 곰방대 as “long-stemmed tobacco pipe.”",
    "Render 건청궁 as “Qianqing Palace.”"
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 태원진가   | **Jin Family of Taiyuan**        |
| 무림맹    | **Murim Alliance**               |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 중원     | **Central Plains**                               |                                                       |
| 전각     | **pavilion**                                 | Use “hall” only when established for a specific named building |
| 시스템              | **System**                     |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 태원     | **Taiyuan**            |
| 정마대전   | **Great Faction War**         |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 마삼보 | **Ma Sanbao** | The East Depot’s Brush-Holding Eunuch and second-in-command. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 열화 | **Blazing Flame** | Lineage term in Taekyung's declaration as the Fire King's successor. |
| 열화신룡 | **Blazing Flame Divine Dragon** | New sobriquet bestowed on Jin Taekyung. |
| 의지 | **Will** | System attribute that replaces Endurance after its dramatic increase. |
| 신룡 | **Divine Dragon** | Title used when discussing the Water God Dragon's intentions. |
| 호법 | **stand guard** | Mungyeong offers to protect Jeok during cultivation. |
| 인자 | **ninja** | Japanese assassin skilled in concealment and concealed weapons. |
| 사냥개 | **hunting dog** | Jin's demeaning metaphor for Ares personnel who obey Go Jun. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 화신 | **Fire God** | A local deity worshiped by one Nanman believer. |
| 금의위 | **Embroidered Uniform Guard** | Imperial guard force mentioned by Hong Jin. |
| 동창 | **East Depot** | Imperial agency named by Hong Jin. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 혁무진 | 조장님 | pavilion_member_to_squad_leader | Captain | deferential and dubious | Mujin questions whether the pasture should be called the Nanman Ranch instead of the Nanman Beast Palace. |
| 홍진 | 혁무진 | imperial aide addressing a martial artist accompanying the prince | Martial artist Hyuk | polite and conversational | Uses 혁 무인 when asking whether Mujin knows of an exception. |
| 홍진 | 마삼보 | Longtime friend and former East Depot cohort | Ma Constable; Eunuch Ma | Familiar and respectful | Hong uses both forms while acknowledging Ma’s former and current standing. |
| 마삼보 | 홍진 | Longtime friend and former East Depot cohort | Hong Constable | Familiar and respectful | Ma addresses Hong by his former East Depot title. |

## Listed compact profiles

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 866
- **Aliases:** None
- **Role:** Hong Jin is a Level 22 Deputy Military Commissioner of Shanxi Province, a eunuch and trusted aide to Prince Shangshan, and a former member of the East Depot.
- **Personality:** Composed, socially deft, and ambitious, Hong Jin became a eunuch to escape poverty and save his family, then used his abilities to pursue a broader life.
- **Voice:** Delicate and deferential, using formal, self-effacing language with Prince Shangshan.
- **Relationships:** Hong Jin is devoted to Prince Shangshan, whom the late Emperor entrusted to his care, and trusts Jin Taekyung to help protect him; he is a longtime friend and ally of Ma Sanbao, his former East Depot cohort.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 865
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; loyal even when left behind, irreverently self-deprecating, and willing to face danger rather than abandon the person he serves. He is proud, glory-seeking, suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad; as a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 860
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, the occupant of the chief seat of the Murim Alliance's Five Kings Hall, and a trusted confidant who accepts Jin as himself despite knowing that he travels between Murim and another world resembling the realm of immortals.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He deeply trusts his publicly acknowledged Disciple and intended heir Jin Taekyung, warmly regards Ju Hwaran and hopes she and Jin grow closer, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and remains Peng Cheolhu's rival.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 867
- **Aliases:** Blazing Flame Divine Dragon; Apostle of the Earth Mother Goddess; Sleeping Dragon of Shanxi; Tollgate Hero; Hong Gil-dong (temporary false identity); youngest son of the Jin Family of Taiyuan
- **Role:** Jin Taekyung is the Third Young Master of the Jin Family of Taiyuan, Jeok Cheongang’s Disciple, the Fire Gate Clan’s nineteenth successor, Pavilion Master of the Fire Dragon Pavilion, a Supreme Peak master and publicly recognized S-rank-level Hunter with an A-rank license, a traveler between Murim and another world, and the World Hunter Federation’s Alliance Leader.
- **Personality:** Hungry, self-aware, dryly observant, and pragmatic under pressure; accepts extreme personal risk when duty and the lives of others demand it.
- **Voice:** First-person, conversational, dryly self-mocking, with vivid trap-and-prey imagery, game terminology, and occasional profanity.
- **Relationships:** Jin Mukyung is his older brother, and Jeok Cheongang is his Master and trusted confidant; they trust each other deeply, though their bond remains unformalized. Cheongpung is his trusted companion and only true martial rival; Choi Minwoo is his subordinate and trusted manager of media and official arrangements as well as the Peace Guild's Guild Master; Ju Hwaran is a trusted Fire Dragon Pavilion member; Magic Johnson and Chuck Hagel are allied to him; his mother and sister Hayeon are among those he protects; the Skeleton King is his friend and ally; Xiao Shen regards him as an older brother; Jin-ho is his older friend and trusted confidant; he once saved Ju Wongong’s life.

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 867
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Ma Sanbao.md

# Ma Sanbao (마삼보)

- **Safe through:** Chapter 866
- **Aliases:** None
- **Role:** Ma Sanbao is the East Depot’s Brush-Holding Eunuch and second-in-command, a Supreme Peak martial artist who has secretly remained in the imperial palace.
- **Personality:** He is vigilant and patient, concealing his loyalties while awaiting the moment to act for the late Emperor.
- **Voice:** He speaks casually and directly with longtime companions, while remaining alert and controlled with new acquaintances.
- **Relationships:** Ma Sanbao is a longtime friend and former East Depot cohort of Hong Jin; he is loyal to the late Emperor and opposed to the current ruler.

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 867
- **Aliases:** None
- **Role:** Prince Shangshan, whose personal name is Zhu Bao, is an early-adolescent member of the imperial family and an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest and compassionate, he takes responsibility for his loyal subjects’ hardship, admires Jin Taekyung, seeks candid counsel, and shows composure beyond his years in the face of death and political danger.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Prince Shangshan Zhu Bao is the Emperor’s only younger full brother; the late Emperor entrusted Hong Jin with his care, and Zhu Bao admires Jin Taekyung and seeks to emulate him.

## Korean source

```text
＃868화



마삼보가 찾아왔던 그 날 밤.

나는 오랫동안 잠을 이루지 못했다.

하늘이 마치 작정이라도 한 듯, 미친 듯이 퍼부어 대는 빗줄기와 낙뢰 때문만은 아니었다.

처음 나타났을 때처럼 홀연히 떠나 버린 마삼보와 마지막으로 나누었던 대화가 끊임없이 머릿속에서 재생되고 있었다.



‘자네의 도움이 필요하네.’



마삼보가 처음 그렇게 말했을 때, 나는 쉽사리 대답하지 못했다.

이는 부정할 수 없는 역모(逆謀)였으니까.

만약 내가 승낙한다면, 그리고 이 일이 틀어진다면 누구도 뒷일을 장담할 수 없다.

황실과 관련된 이상, 이건 개인의 일탈로 취급될 수 있는 일이 아니다.

열화신룡 진태경이 아니라, 태원진가의 진태경으로서 실패의 대가를 치러야 한다는 사실이 내 마음을 무겁게 만들었다.



‘만약 이 일이 실패한다면, 그때는 어떻게 되는 겁니까?’

‘자네도 이미 알고 있지 않나.’

‘…….’

‘실패하면 역적이요, 성공하면 천자라. 후자라면 천하의 그 누구도 못 누릴 부귀(富貴)와 영화(榮華)가 기다리고 있겠지만, 전자라면 지옥보다도 더한 고통을 겪게 되겠지.’



지금껏 수많은 전투를 치렀고, 헤아릴 수도 없이 많은 적을 쓰러트렸다.

그중에는 손가락 하나로 상대할 수 있을 정도의 약자도, 손가락 하나 까딱할 수 없을 만큼 두려웠던 강적도 있었다.

하지만…… 이번 일은 다르다.

천하의 주인은 대국이며, 대국의 주인은 천자다.

바로 그 천자를 상대로 반기를 든다는 것은, 곧 천하 그 자체와 싸워야 한다는 뜻이다.

나는 물론이고 내 주위의 모두가.



‘잘 생각하게. 물론 자네가 상산왕 전하를 비호하기 위해 황궁에 발을 디딘 이상, 이미 모든 것이 늦어 버렸을지도 모르지만.’

‘지금, 날 협박하는 겁니까?’

‘아니, 협박이 아닌 진실이지.’



마삼보. 동창의 이 인자가 보였던 그 서슬 퍼런 눈빛이 아직도 눈앞에 선했다. 깊게 가라앉아 있던 그의 목소리도.



‘지난 반정으로 죽은 이들의 숫자가 얼마나 될 것 같나? 사약을 받고, 귀양지로 끌려가는 길에 알 수 없는 이유로 죽고, 저잣거리에서 사지가 찢겨 죽거나 효수(梟首)를 당한 이들만 수만 명일세. 이 세상에 알려진 것만 그 정도일진대, 드러나지 않은 죽음은 어느 정도일까. 그리고 그중 자네처럼 아무런 연관도 없던 자들은 몇이나 되었을까?’

‘……!’

‘지록위마(指鹿爲馬)라고 했네. 결국 모든 것은 황제의 뜻에 달렸어. 멀쩡한 사슴이 말이 되듯이, 자네 역시 얼마든지 역적이 될 수 있음을 명심하게.’



권력자들의 변덕과 의심은 역사가 증명한다.

그리고 작금의 천자는 세상 그 누구도 부정할 수 없는 폭군(暴君)이었다. 순리를 거스르고 핏물을 밟으며 황위에 오른 반역자이자 절대적인 권력을 휘두르는 지배자.

그렇기에 마삼보의 말을 듣는 순간 나 역시 어렴풋이 깨달았다.

역적이 되고 말고는, 이미 내 손을 떠났을지도 모른다는 사실을.



‘물론 나 역시 그들의 죽음에 한 손을 거들었음을 부정하지는 않겠네. 아니, 오히려 앞장섰지. 그렇게 해서라도 반드시 살아남아야 했으니까. 나만큼은 이 자리에 남아서 때를 기다려야 했으니까.’



어느 누군가는 어린 주인을 섬기기 위해 황궁을 떠났고, 또 다른 누군가는 언젠가 돌아올 주인을 맞이하기 위해 그곳에 남았다.

홍진이 전자였다면, 마삼보는 후자였다.

그는 곧 사 황자, 아니 새로운 황제의 사냥개가 되었다.

누구보다 잔인하고, 가차 없이 표적의 목덜미를 물어뜯으며 잔혹했던 숙청에서 살아남아 동창의 이 인자인 병필태감의 자리까지 올랐다.

그리고 그와 같은 방식으로 살아남은 것은, 비단 마삼보 한 사람뿐만이 아니었다.



‘모두가 모인 그날 밤, 창공(廠公) 어른께서 말씀하셨네. 지금까지의 동창이 어둠 속에 핀 꽃이었다면, 이제부터는 잡초가 되어야 한다고.’



빛이 있건 없건 꽃은 화려하며 아름답다.

하지만 잡초는 아니다. 볼품없고 이름도 없는 풀 따위에는 그 누구도 눈길을 주지 않는다.

또한 그렇기에, 더 오래 살아남는다.

동창의 수장인 장인태감(掌印太監). 즉 창공은 뜻을 함께하는 동지들에게 바로 그런 잡초가 되어 살아남기를 종용했다.

긴 세월과 함께 찾아온 병마(病魔)를 이기지 못해 쓰러지기 전까지는.



‘지금으로부터 오 년 전, 창공 어른께서 병석에 자리하신 뒤부터는 내가 모두를 이끌기 시작했네. 연판장(連判狀)을 만든 것도 그때부터지.’



연판장.

역적들이 자신들의 피로 서명한 명백한 증거이자, 어쩌면 향후 새로운 천자를 옹립할 공신(功臣)들의 이름이 적힌 역사의 기록.

마삼보는 그 연판장을 언급하며 떠났다.

나로 하여금 밤을 지새우게 만들 수밖에 없었던 마지막 한 마디와 함께.



‘암천(暗天). 현재 무림을 뒤흔들고 있는 그들에 대해 알고 있네. 아마 자네가 짐작하는 것보다 훨씬 더 깊고 자세하게.’

‘……!’

‘자네가 이대로 떠난다 해도 구태여 붙잡지 않음세. 하지만 우리를 도와 상산왕 전하를 옹립한다면, 새로운 질서를 바로 세운다면…… 그에 마땅한 보상을 해 주어야겠지.’



마삼보는 그렇게 떠났고, 홍진은 어린 왕의 곁으로 돌아갔으며, 나는 그 자리에 남아 생각에 잠겼다.

창가로 새벽녘의 서광(曙光)이 닿을 때까지.

서서히 잦아드는 빗줄기와 함께 저 멀리 동이 터 올 때까지.

그리고 지금 이 순간까지.

“이런 시발.”

나도 모르게 불쑥 튀어나온 욕설에, 한구석에서 꾸벅꾸벅 졸고 있던 혁무진이 화들짝 놀라며 깨어난다. 자리에서 벌떡 일어난 녀석이 반쯤 감긴 눈으로 품 안의 검을 더듬거렸다.

“습격입니까? 습격이에요? 이놈들! 감히 어떤 새끼들이…….”

“무진아.”

“예?”

“자라.”

“예.”

언제 그랬냐는 듯 철푸덕 주저앉은 혁무진은 금세 다시 잠들었다.

아무리 황도까지 오는 길이 피곤했어도 그렇지, 저 자세로 꼬박 네 시진을 처자는 것도 재주라면 재주다.

드르렁.

“…….”

아무리 그래도 코골이는 선 넘었지.

빡!

“으헉! 이놈들! 조장님 몸에는 손끝 하나 댈 수 없다!”

“무진아.”

“예?”

“호법이라는 새끼가 그 정도로 깊게 잠들면 털끝 하나 빼고 다 손댔겠다.”

“헉, 어떤 놈이 이미 조장님께 손을 댄 겁니까? 아닙니다. 굳이 말씀하실 필요 없어요. 홍진 그 인간이죠? 내가 그럴 줄 알았어. 어쩐지 평소에 조장님을 바라보던 눈빛부터가 음탕…….”

“무진아. 이 시벌 새끼야……!”

나는 가슴 깊이 우러나오는 한탄을 토해 냈다.

하필이면 이런 놈이 내 오른팔, 아니 새끼발가락이라니.

안 그래도 심각한 상황인데 녀석까지 저 지경이니 현자 타임이 제대로 온다. 이 정도면 암천이 일찍 세상을 떠나라고 붙여 놓은 우화등선 청부사가 아닐까 의심이 될 정도다.

‘시스템도 없고, 당장 의지할 만한 사람도 없고.’

생각해 보면 지금까지의 나는 퍽 운이 좋은 편이었다.

시스템은 모호하게나마 늘 퀘스트를 통해 가야 할 길을 알려 주었고, 적천강은 내가 흔들릴 때마다 믿고 기댈 수 있는 든든한 버팀목이었으니까.

그러나 지금 내 곁에는 그중 무엇도 없다.

앞으로 벌어질 모든 일은 오직 지금의 내 선택에 달렸다.

‘실패하면 역적이요, 성공하면 천자라.’

마삼보가 했던 그 말이 환청처럼 귓가를 맴돈다. 그의 마지막 한 마디도 함께.



‘암천(暗天). 현재 무림을 뒤흔들고 있는 그들에 대해 알고 있네. 아마도 자네가 짐작하는 것보다 훨씬 더 깊고 자세하게.’



정확히 무엇을, 어떻게 그리 잘 아는지. 당신이 알아냈다는 암천에 대한 정보와 천자가 어떤 연관이 있으며 얼마나 위험한지.

어떻게 해서든 떠나려는 마삼보를 붙잡고 더 캐묻고 싶었지만, 소란과 동시에 버스터콜을 받고 달려올 금의위를 생각해서 꾹 참아야 했다.

아니, 어쩌면 그 뒤에 이어졌던 말에 담긴 무게감을 생각하느라 그를 놓쳤을지도 모른다.

‘보상. 보상이라…….’

나는 조용히 그 단어를 곱씹었다.

마삼보는 분명히 그리 말했다. 자신들을 도와 상산왕을 새로운 천자로 옹립한다면, 그에 마땅한 보상이 주어질 것이라고.

그리고 앞서 암천을 언급한 것을 보았을 때, 그가 말하는 보상이 무엇인지 짐작하는 것은 그리 어려운 일이 아니었다.

‘황실이, 대국(大國)이 무림맹을 도와 암천을 토벌한다.’

관과 무림은 불가침이라는 말이 괜히 있던 것이 아니듯, 대국은 지금껏 무림의 일에 깊게 관여하지 않았다.

아니, 현재에 이르러 생각해 보면 그 이유는 너무나도 명백했다.

‘구태여 끼어들 만한 이유가 없었으니까.’

천하를 통틀어 셈할 필요도 없다. 황도 인근에만 무려 백만에 달하는 정예군이 주둔해 있으며 내가 두 눈으로 확인한 절정 고수만 무려 수백이다.

여기에 더하여 아직 드러나지 않은 전력. 특히 초절정 고수까지 포함한다면…….

‘황도의 전력만으로도, 이미 무림맹을 아득히 넘어선다.’

물론 대국의 전력 대부분이 황도에 집중되어 있음은 부정할 수 없다.

이민족들의 침략을 비롯한 모든 전란은 이미 오래전에 끝났고, 통일 왕조의 황제들은 천하 각지에 흩어져 있는 성주들이나 번왕에게 필요 이상의 병권(兵權)을 쥐여 주지 않았으니까.

다만 그들은 단지 이 거대하고 단단한 성벽 위에서 모든 것을 내려다보았을 뿐이다.

세인들이 무림이라 칭하는, 대국이라는 울타리 안에 존재하는 또 다른 울타리에서 벌어지는 치열한 힘겨루기를.

이는 정마대전(正魔大戰)이 벌어졌을 때조차도 예외가 아니었다.

‘하지만 바로 그 대국이, 무림맹의 손을 들어 준다면.’

승리의 저울추가 단번에 기운다.

지금까지의 흐름이 중원 무림과 암천과의 싸움이었다면, 대국의 합류 이후에는 암천이 바로 천하가 적대시하는 외적(外敵)이다.

비록 아직까지 드러나지 않은 암천의 전력이 어느 정도인지는 가늠할 수 없지만, 대국이라는 두 글자에 실린 무게감은 그만큼 무겁고 확실한 것이었다.

물론 가장 치명적인 한 가지 문제가 있다면…….

‘실패했을 때지.’

하이 리스크. 하이 리턴.

실패하면 역적이요, 성공하면 천자라.

마치 벼랑 끝에 서 있는 듯한 기분이다.

천자라는 날개를 얻어 구름 위로 날아갈 수도 있지만, 반대로 천자에 의해 두 다리가 부러진 채 낭떠러지 아래로 추락할 수도 있다.

나뿐만 아니라 모두가.

드르렁.

“…….”

그래, 이 새끼도 포함해서.

“……무진아. 이 새끼야.”

자연스럽게 눈을 뜬 혁무진이 입을 열었다.

“저 안 잤습니다.”

“그래?”

“예.”

“그런 것치고는 코 고는 소리가 존나게 우렁차던데. 조금 있으면 금의위가 올라와서 잡아가겠다. 너 새끼 코 고는 소리에 황제 깼다고.”

“진짭니다.”

“어떻게 증명할래?”

눈깔을 뒤룩뒤룩 굴리던 혁무진이 입을 열었다.

“홍진의 불알을 걸겠습니다.”

“…….”

아니, 이 새끼가 없는 걸 걸려고 하네.

생각지도 못한 대답에 할 말을 잃은 그때, 낯익은 금속음이 창밖으로 들려왔다.

철컥. 철컥.

질서정연한 움직임과 날선 기세.

금의위다.

전각으로 진입하는 황금빛 갑옷들을 바라보던 혁무진이 놀란 얼굴로 물었다.

“진짜 저 때문에 황제가 잠에서 깬 겁니까?”

“…….”

진짜 죽일까.

한숨을 푹 내쉰 내가 말했다.

“상산왕 전하나 모셔와.”

아무래도, 때가 된 모양이다.
```

## Final English reading copy

```markdown
# Chapter 868

The night Ma Sanbao came to see me.

I couldn’t sleep for a long time.

It wasn’t just because of the rain pouring down like the heavens had made up their minds to unleash it, or the lightning striking all around us.

The last conversation I’d had with Ma Sanbao kept replaying in my head. He’d vanished as suddenly as he had appeared.

*I need your help.*

When Ma Sanbao first said those words, I couldn’t give him an answer.

This was an undeniable plot against the throne.

If I agreed, and things went wrong, no one could say what would happen next.

With the imperial family involved, this couldn’t be dismissed as one person’s wrongdoing.

The thought that I wouldn’t pay the price for failure as the Blazing Flame Divine Dragon Jin Taekyung, but as Jin Taekyung of the Jin Family of Taiyuan, weighed heavily on me.

*What happens if this fails?*

*You already know, don’t you?*

*……*

*Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven. If you succeed, unimaginable wealth and glory await you—things no one else in the world could enjoy. But if you fail, you’ll suffer a pain worse than hell.*

I’d fought countless battles and brought down more enemies than I could count.

Some had been so weak I could take them on with one finger. Others had been so terrifying I could barely move a finger against them.

But…… this was different.

The Great Nation was the master of the world, and the Son of Heaven was the master of the Great Nation.

To rebel against that very Son of Heaven meant fighting the world itself.

Me—and everyone around me.

*Think carefully. Of course, since you set foot in the imperial palace to protect His Highness Prince Shangshan, it may already be too late for you.*

*Are you threatening me?*

*No. I’m telling you the truth.*

Ma Sanbao. The East Depot’s second-in-command. The cold, piercing gaze he’d fixed on me was still vivid before my eyes. So was his deep, sunken voice.

*How many people do you think died in the coup? Tens of thousands were executed by poison, died for unknown reasons on the way to exile, were torn limb from limb in the marketplace, or had their heads displayed. That’s only the number the world knows about. How many deaths were never brought to light? And how many of them had nothing to do with it, like you?*

*……!*

*They call it “calling a deer a horse.”[^1] In the end, everything depends on the Emperor’s will. Just as a perfectly ordinary deer can become a horse, you, too, can be made a traitor. Keep that in mind.*

History had proven the fickleness and suspicion of those in power.

And the current Son of Heaven was a tyrant no one in the world could deny. A usurper who had defied the natural order and waded through blood to claim the throne, a ruler wielding absolute power.

So the moment I heard Ma Sanbao’s words, I understood, if only vaguely:

Whether I became a traitor might already be out of my hands.

*Of course, I won’t deny that I helped bring about their deaths. No—I led the way. I had to survive, no matter what it took. I had to remain here, of all places, and wait for the right moment.*

Some had left the imperial palace to serve their young master. Others had remained there to welcome him when he returned one day.

Hong Jin had been the former. Ma Sanbao was the latter.

He became the fourth prince’s—no, the new Emperor’s—hunting dog.

He was one of the cruelest of them, sinking his teeth into his targets’ necks without mercy. He survived that brutal purge and rose to become the East Depot’s second-in-command, its Brush-Holding Eunuch.

And Ma Sanbao wasn’t the only one who survived that way.

*That night, when we all gathered, the Director said that if the East Depot had been a flower blooming in the dark until then, from that point on we had to become weeds.*

Flowers were colorful and beautiful, whether they bloomed in the light or the dark.

Weeds weren’t. No one paid any attention to plain, nameless grass.

And because of that, it survived longer.

The Director, the East Depot’s head and its Seal-Holding Eunuch, had urged his like-minded comrades to survive by becoming weeds like that.

Until he finally fell, unable to overcome the illness that came with his long years.

*Five years ago, after the Director took to his sickbed, I began leading everyone. That was when I started drawing up the blood-signed pact.*

The pact.

Clear proof that the traitors had signed their names in their own blood—and perhaps a record of the names of the meritorious officials who would one day enthrone a new Son of Heaven.

Ma Sanbao mentioned the pact, then left.

And with one last remark that could only keep me up all night.

*Dark Heaven. I know about the people currently throwing Murim into turmoil. Probably far more deeply and thoroughly than you suspect.*

*……!*

*Even if you leave now, I won’t go out of my way to stop you. But if you help us enthrone His Highness Prince Shangshan and set a new order in place…… we’ll have to give you an appropriate reward.*

Ma Sanbao left. Hong Jin returned to the young prince’s side, and I stayed where I was, lost in thought.

Until the first light of dawn reached the window.

Until the rain slowly began to let up and day broke in the distance.

And until this very moment.

“Fuck.”

At my sudden curse, Hyuk Mujin, who’d been nodding off in a corner, jolted awake. He leaped to his feet and fumbled for the sword in his arms, eyes half shut.

“Are we under attack? An attack? You bastards! How dare you—”

“Mujin.”

“Yes?”

“Go to sleep.”

“Yes.”

Hyuk Mujin flopped back down as if nothing had happened and fell asleep again in no time.

The trip all the way to the imperial capital must have been exhausting, but sleeping for four whole *shichen* in that position was a talent in itself.

*Snore.*

“……”

Even so, snoring was crossing the line.

*Whack!*

“Ugh! You bastards! No one lays a finger on the Captain!”

“Mujin.”

“Yes?”

“If my bodyguard sleeps that soundly, they could lay hands on every part of me but a single hair.”

“Gasp! Someone’s already laid a hand on the Captain? No, you don’t even have to tell me. It was Hong Jin, wasn’t it? I knew it. The way he looked at you was lecherous from the start……”

“Mujin. You little shit……!”

I let out a groan that came from the depths of my soul.

Of all people, this idiot was my right-hand man—or rather, my pinky toe.

Things were serious enough as it was, and with him like this, I’d hit a proper moment of clarity. At this point, I was starting to wonder if Dark Heaven had sent him as an ascension-to-immortality hitman to make sure I left this world early.

*No System, and no one I can rely on right now.*

Thinking about it, I’d been pretty lucky until now.

The System had always pointed me toward where I needed to go, even if it did so vaguely through Quests. And whenever I wavered, Jeok Cheongang had been a sturdy pillar I could trust and lean on.

But now I had neither.

Everything that happened from here on would depend solely on the choices I made.

*Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven.*

Ma Sanbao’s words circled in my ears like an echo. His final remark came with them.

*Dark Heaven. I know about the people currently throwing Murim into turmoil. Probably far more deeply and thoroughly than you suspect.*

What exactly did he know, and how had he learned so much? What connection did the information he’d uncovered about Dark Heaven have to the Son of Heaven—and how dangerous was it?

I’d wanted to stop Ma Sanbao, who seemed determined to leave, and press him for more answers. But I held back, imagining the Embroidered Uniform Guard receiving a Buster Call and rushing over the moment I caused a commotion.

No—or maybe I’d let him go because I was weighing the significance of what he’d said next.

*Reward. A reward……*

I quietly turned the word over in my mind.

Ma Sanbao had said it plainly. If I helped them enthrone Prince Shangshan as the new Son of Heaven, they would give me a fitting reward.

And given that he’d mentioned Dark Heaven just before, it wasn’t hard to guess what kind of reward he meant.

*The imperial family—the Great Nation—helps the Murim Alliance wipe out Dark Heaven.*

There was a reason people said the government and Murim must never interfere with one another. The Great Nation had never involved itself deeply in Murim’s affairs.

No, thinking about it now, the reason was obvious.

*There was no reason for them to get involved.*

There was no need to count the forces across the entire world. A million elite troops were stationed near the imperial capital alone, and I’d seen hundreds of Peak masters with my own eyes.

And if you included the forces that hadn’t yet come to light—especially the Supreme Peak masters……

*The imperial capital alone already dwarfs the Murim Alliance in strength.*

Of course, it was undeniable that most of the Great Nation’s forces were concentrated in the imperial capital.

All the wars, including invasions by foreign tribes, had ended long ago. The emperors of the unified dynasty had never given the lords and vassal princes scattered across the land more military power than necessary.

They had simply watched everything from atop these enormous, impregnable walls.

They watched the fierce struggle for power taking place in another enclosure within the Great Nation’s borders—the one people called Murim.

That had been true even during the Great Faction War.

*But if the Great Nation itself took the Murim Alliance’s side……*

The scales of victory would tip in an instant.

Until now, the fight had been between the Central Plains’ Murim and Dark Heaven. If the Great Nation joined in, Dark Heaven would become an external enemy hated by all under heaven.

I still couldn’t gauge how powerful Dark Heaven’s forces were, since so much remained hidden. But the weight carried by the two words “Great Nation” was just as heavy—and undeniable.

Of course, there was one fatal problem……

*What if we failed?*

High risk. High reward.

Fail, and you’re a traitor. Succeed, and you’re the Son of Heaven.

It felt like standing at the edge of a cliff.

I could gain the wings of the Son of Heaven and soar above the clouds. Or the Son of Heaven could break both my legs and send me tumbling off the precipice.

And not just me. Everyone.

*Snore.*

“……”

Right. That included this idiot, too.

“……Mujin. You little shit.”

Hyuk Mujin opened his eyes naturally and spoke.

“I wasn’t asleep.”

“Is that so?”

“Yes.”

“Then why was your snoring so damn loud? The Embroidered Uniform Guard will come up and haul you away soon. The Emperor woke up because of your snoring.”

“I’m serious.”

“How are you going to prove it?”

Hyuk Mujin’s eyes rolled around before he answered.

“I’ll stake Hong Jin’s balls.”

“……”

This idiot was trying to stake something that didn’t exist.

I was at a loss for words when I heard a familiar metallic sound outside the window.

*Clack. Clack.*

Orderly movement. A sharp aura.

The Embroidered Uniform Guard.

Hyuk Mujin stared at the golden-armored guards entering the pavilion and asked, wide-eyed,

“Did the Emperor really wake up because of me?”

“……”

Should I really kill him?

I let out a deep sigh, then said,

“Go bring His Highness Prince Shangshan.”

It looked like the time had come.

[^1]: An idiom meaning to deliberately distort the truth or impose a false label.
```
