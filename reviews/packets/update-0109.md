<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0109.txt",
      "sha256": "2d034eb251aa2f6e4d5eda4c1db90332edcd83327de295359b0cfda9f654db27",
      "bytes": 13343
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "fff0e7d3fa33da37ad4dc8708e36055fbf8f03cc60375dae8fc4a935afd01cf8",
      "bytes": 2928
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "cdf192e20f652dfb063b1d7e99878191d61cc7d50f9a0838b673ebb422e6c2a3",
      "bytes": 14549
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "b78e0d8cce8c955fddbfdd28be61ae7974503e039b5fd7d971470c3637a13969",
      "bytes": 5130
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "784fdaed7ef855b15a5d7004eb24e6150b76b7f693adf45e100ceb068a7ecc3c",
      "bytes": 1221
    },
    {
      "path": "characters/Lee Cheonbaek.md",
      "sha256": "81795f47083fb2685d155aa52fc0a6f6f4459f8d85fb735d53470efdb06fdfb0",
      "bytes": 3101
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "83ac35f0e4b0ca6636b96bb5e1efeb8c1dd330f511a5529e799f4e38ce978eb5",
      "bytes": 2246
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a0b927c08fc350fdf09937274b8cb2ab74ca088a427708c0f16163c887cf12ac",
      "bytes": 14625
    }
  ],
  "estimated_tokens": 16891
}
-->

# Durable State Update — Chapter 109

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 109. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 109. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 109,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 109,
    "continuity_sources": [109],
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
    "Taekyung, Mukyung, Mujin, and Wolhwa are traveling toward the Mount Heng Sword Sect and sheltered in an abandoned shrine.",
    "Ten armed human traffickers led by Lee Sam arrived at the shrine with five captives.",
    "The captives were the Five-Colored Ghosts, former subordinates of Jang Sam who had quit banditry but recently committed theft.",
    "Taekyung freed the Five-Colored Ghosts despite their criminal past.",
    "Mukyung defeated the traffickers in seconds, crippling Lee Sam and forcing the rest to surrender.",
    "Lee Sam’s Level fell from 25 to 2 after Mukyung destroyed his limbs and dantian.",
    "The traffickers identified the Red Wind Band as the mounted-bandit group traveling toward Saneum.",
    "The Red Wind Band planned to leave at dawn and travel nonstop to Saneum, near Eung-hyeon.",
    "A messenger hawk carrying a cylinder arrived at the shrine, but its sender and message are unknown."
  ],
  "continuity_sources": [
    108
  ],
  "open_questions": [
    "Which of the three recently traded properties is being used by the surveillance personnel?",
    "Whether the black Familiar and Kim Gwondong are operating under the same immediate instructions remains unresolved.",
    "Why Kim Hwajong arrived at the confrontation remains unknown.",
    "Why Kim Hwajong now works as a butler despite his former instructor status and exceptional ability remains unexplained.",
    "What final disciplinary action will be taken against the Security Team remains unknown.",
    "How and why Seong Jinho entered the capsule and emerged inside Taekyung’s new house remains unknown.",
    "How Lee Seowol and Mount Heng will respond to the merger proposal, and what compensation or territorial concession Wolhwa will receive, remain unresolved.",
    "Who sent the messenger hawk and what message its cylinder contains remain unknown."
  ],
  "safe_through": 108,
  "temporary_decisions": [
    "Use mouth-sealing technique for 아가리 봉인술 and keep Fire Wall as the spell name.",
    "Render Im Chunsoo’s 자네 as you; render 김화종’s 춘수 and 교관님 as Chunsoo and Instructor; render 1번 훈련생 as Trainee Number One; render 열양공 as heat-yang technique.",
    "Render 원단 as Lunar New Year.",
    "Render 봉황객잔 and 계용옥미갱/계용옥미앵 as Phoenix Inn and chicken-and-corn soup.",
    "Render 곡도 as curved saber.",
    "Render 마적 and 마적단 as mounted bandits and mounted-bandit groups; render 적풍단 as Red Wind Band.",
    "Render 초일류 as master beyond First Rate; preserve Wolhwa’s playful Young Master forms for Taekyung and use Young Hero Jin for her 진 소협 address to Mukyung; render 관제묘 as Guandi Temple and 흑도 as dark-path figures.",
    "Render 오색귀 as Five-Colored Ghosts, 이삼 as Lee Sam, 전서응 as messenger hawk, and 대형 as Boss."
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진무경    | **Jin Mukyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 이천백    | **Lee Cheonbaek**  |
| 월화     | **Wolhwa**         |
| 진천검    | **Heaven Shaking Sword**      | Jin Mukyung    |
| 혈랑검    | **Blood Wolf Sword**          | Lee Cheonbaek  |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 하오문    | **Lower District Sect**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 돌파     | **break through** / **breakthrough**             | Realm advancement                                     |
| 낭인     | **wandering martial artist**                     |                                                       |
| 강호     | **martial world**                                | Prefer “Murim” where the setting itself is meant      |
| 마적     | **mounted bandits**                              |                                                       |
| 문주     | **Sect Leader**                              |
| 대주     | **Squad Leader** / **Commander**             |
| 지부장    | **Branch Leader**                            |
| 일격     | **One Strike**                         |
| 퀘스트              | **Quest**                      |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 삭주 | **Sakju** | Jin Family branch location |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |

## Listed compact profiles

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 108
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a tenant-farmer family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 108
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Lee Cheonbaek.md

# Lee Cheonbaek (이천백)

- **Safe through:** Chapter 107
- **Aliases:** Blood Wolf Sword
- **Role:** Sect Leader of the Mount Heng Sword Sect; Lee Seogeun’s father
- **Personality:** Grief-stricken, resolute, and fiercely vengeful
- **Voice:** Quietly mournful when addressing his son; firm and uncompromising when declaring revenge
- **Relationships:** Father of Lee Seogeun and Lee Seowol; also father of a deceased Young Sect Leader; leader of the Mount Heng Sword Sect

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 108
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, and quietly amused; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear

## Korean source

```text
＃109화



전서응(全書鷹).

태원진가에도 두 마리밖에 없다는 연락용 매다.

훈련시키기 어렵다 보니 중요한 정보를 전달하는 데에만 쓰인다고 들었는데…….

‘누가 보낸 거지?’

전서응을 향해 다가가려는 나를 붙잡은 건 월화의 목소리였다.

“물러서는 게 좋을걸요? 경계심이 심한 녀석이라 진 공자가 잡으려고 들면 도망칠 테니까.”

“아, 혹시?”

“본문에서 보낸 전서응이에요. 특정한 추종향(追從香)을 쫓아오도록 훈련되어 있죠.”

월화가 품에서 자그마한 주머니를 꺼내 흔들자, 전서응이 슬금슬금 다가와 부리를 비빈다.

그 틈에 어느새 밖으로 나온 하오문도가 전서응의 발목에 묶인 원통을 풀었다.

“어디야?”

“하루 전 삭주지부에서 지부장님 앞으로 보낸 전서입니다.”

“이리 줘.”

전서를 건네받아 읽는 월화의 표정이 오묘했다.

굳게 다물어져 있던 입술이 열린 것은 잠시 후였다.

“적풍단주…… 생각 이상인데.”

“또 적풍단에 관련된 겁니까?”

작게 고개를 끄덕인 월화가 내게 전서를 내밀었다.

읽어 보라는데 굳이 마다할 필요가 있나, 쭈뼛거리던 진무경과 혁무진도 슬쩍 고개를 들이밀었다.



적풍단, 고원을 넘어 남하 중. 숫자는 대략 이백으로 추정.



짤막한 한 줄이 의미하는 바는 명백했다.

“다시 한번 항산검문을 치려는 거군요.”

“틀림없어요. 하루 전 소식이니 그만큼, 아니 그 이상으로 거리가 좁혀졌을 거고요.”

현재 항산검문까지 남은 거리는 하루하고도 반나절.

마적단인 만큼 뛰어난 기동력으로 목적지를 향해 진군하고 있을 것이다.

“안타깝게도 저희 지부는 북부에 제대로 된 정보망을 갖추지 못했어요. 그나마 다행인 건…….”

월화의 시선이 적풍단의 마적들을 향했다. 이미 오래전 전의를 상실한 그들은 움찔하며 고개를 숙였다.

“여기 소중한 정보원들이 있다는 거죠. 쓸 만한 정보를 갖고 있을지는 모르겠지만.”

마적들을 훑어보던 그녀가 돌연 한 사람을 지목했다.

“너, 일어나.”

“……저, 저 말입니까?”

잔뜩 겁먹은 얼굴로 일어난 그는 생각 이상으로 젊은 청년이었다. 마적 중 가장 어리고 약한 그 녀석은 월화의 시선을 정면으로 쳐다보지도 못했다.

“나이가?”

“오, 올해 약관을 넘겼습니다.”

“약관? 어리네. 하긴, 어리다고 마적이 될 수 없는 건 아니니까.”

“전 마적이 아닙니다! 얼마 전에 낭인이 되었는데 한몫 단단히 챙겨 준다는 말에 그만…….”

“아, 지난번 습격 때 적풍단주가 끌어모은 낭인 중 하나구나?”

“예, 예! 제가 아는 사실은 모두 말씀드리겠습니다!”

“아냐, 괜찮아.”

“예?”

“별로 아는 것도 없어 보이는데 뭘. 안 그러니, 춘삼아?”

지금까지 묵묵히 마부를 자처하던 하오문도.

그가 대답 대신 품에서 꺼낸 소도(小刀)를 청년의 가슴에 박아 넣었다.

푹-

일류 무인의 빠르고 정확한 일격이 심장을 갈랐다. 비명도 지르지 못한 채 입을 벙긋거리던 청년이 실 끊어진 인형처럼 쓰러졌다.

쿵.

싸늘한 적막이 장내를 짓눌렀다. 경악과 공포로 물든 마적들의 시선 속에서, 월화의 가느다란 손가락이 다시 한번 움직였다.

“너.”

“마, 말하겠소! 전부 다 말하겠소! 나는 적풍단에 일 년째 몸담고 있는…….”

“춘삼아.”

쐐애애액! 서걱!

“크륵, 그르륵.”

마적이 피가래 끓는 소리와 함께 뒷걸음질 쳤다. 쩍 벌어진 목을 막아 보지만 손가락 사이로 뿜어져 나오는 피분수를 막을 수는 없다.

“단 두 가지만 명심하면 돼.”

머리부터 발끝까지.

선홍빛 핏물을 뒤집어쓴 월화가 건조한 어조로 말을 이었다.

“대답은 묻는 말에만, 있는 사실 그대로.”

“……!”

우리는 불과 촌각(寸刻) 만에 적풍단에 관한 모든 정보를 얻을 수 있었다.



* * *



한시가 급하다는 걸 알게 된 우리는 마차를 버리고 말을 한 마리씩 골라잡았다. 나, 진무경, 혁무진, 그리고 월화.

하오문도는 오색귀와 생존한 마적들을 데리고 가까운 하오문 지부에서 상황을 전달할 것이다.

“너무 잔인했나요?”

월화가 말안장을 올리며 건넨 물음에 나는 턱을 긁적였다.

“솔직히, 조금 놀라긴 했어요.”

항상 여유롭고 장난기 넘치는 모습만 봐서 잠시 잊고 있었다. 그녀도 무림인이라는 사실을.

‘그것도 경륜 있는 무림인이지.’

월화의 나이가 어떻게 되더라?

물어본 적이 없어 잘은 모르지만 서른은 넘지 않을 것이다.

그런 젊은 나이에 산서성 전체를 총괄하는 지부장이 되었다는 것은 그에 걸맞은 결단력을 갖췄다는 뜻이다.

‘잔인하지만 효과적인 방법이었어.’

망설임 없이 두 명을 죽였다. 그것도 파리 잡듯 간단하게.

진무경이 우두머리를 상대로 보여 준 모습도 마적들에겐 두려웠겠지만 죽음에 대한 공포는 그 이상이다.

벼랑 끝으로 내몰린 그들은 필사적으로 정보를 쏟아 내는 수밖에 없었다.

“저라도 술술 불었을 것 같은데요.”

“진 공자가 오해할까 봐 말해 두는데, 살생에는 취미 없어요. 상대가 선량한 양민들도 아니었고…… 아, 이놈의 피는 닦아도 끝이 없네.”

주르륵 흘러내리는 피는 두 번째로 죽은 마적의 것이다.

콧잔등을 찡그리는 그녀를 향해 천 조각을 내미는 한 사람이 있었다.

“이, 이걸로 닦으시오.”

“어머.”

“엥?”

“흐음.”

월화와 나, 그리고 혁무진의 반응에 진무경이 헛기침을 연발했다.

“그, 필요할 것 같아서.”

“고마워요, 진 소협. 마침 딱 필요했는데.”

“별것 아니오.”

말과는 달리 표정은 상당히 뿌듯해 보이는데?

저놈 저거 설마…….

‘여자한테만 잘해 주는 타입이구나.’

어딜 가나 저런 놈이 꼭 하나씩 있지. 천하의 진천검도 별다른 것 없던 모양이다. 그때 피를 닦아 낸 월화가 품에서 돌돌 만 가죽을 꺼내어 펼쳤다.

“산서성 전역을 대략으로 표기한 지도에요. 우리 위치는 지금 여기. 적풍단은 아마…… 쉬지 않고 이동했다면 이미 대동(大同)을 돌파했을지도 모르겠네요.”

“저희보다 빠르군요.”

“지금으로선 반나절. 하지만 우리가 가는 길에는 관도가 잘 정비되어 있으니 밤낮없이 달린다면 충분히 격차를 좁힐 수 있을 거예요.”

요컨대 쉴 생각은 하지 말라는 뜻이다. 나는 사람들을 따라 말안장 위로 훌쩍 뛰어올랐다.

‘어째 오자마자 일이 터지냐.’

내심 한숨이 나왔지만, 별수 있나. 한두 번 고생하는 것도 아니고 이젠 그러려니 해야지.

‘이거 되게 간단한 퀘스트였던 것 같은데.’

띠링.



- 퀘스트 난이도가 [절정]으로 변경되었습니다.



“…….”

어, 그래. 이젠 아니구나.



* * *



여우를 닮은 사내였다. 뾰족한 턱과 귀, 날카롭게 찢어진 눈동자는 주위의 모든 것들을 감시하는 동시에 관찰했다.

“크아아악!”

“죽여라, 싸그리 다 죽여!”

“꺄아아아아!”

커다란 장원에서 솟구치는 연기, 그리고 비명.

말에 올라 언덕 아래를 응시하던 사내, 적풍단주 풍양(風陽)의 입이 열린 것은 장원이 잠잠해진 후였다.

“끝났나?”

보고를 위해 막 언덕을 올라온 마적이 대답했다.

“사내놈들은 전부 죽였고, 아이와 여자들은 한데 모아 뒀습니다.”

“왜?”

“예? 그야 당연히 고원의 전통대로…….”

마차 바퀴보다 큰 사내는 아이라도 가차 없이 죽이고, 여인은 취하거나 노예로 팔아 버린다. 그것이 유목민들로부터 전해져 내려오는 전통 아닌 전통이었다.

마적의 말에 풍양은 조용히 손가락을 까딱였다.

“이리 가까이 와 보게.”

주춤주춤 다가온 마적이 조심스럽게 물었다.

“단주, 제가 혹시 큰 실수라도…….”

“원래 어디 소속이었나?”

“얼마 전까지 토호단에 부단주로 있었습니다.”

“토호단? 아, 기억나. 거기 부단주가 자네였군.”

“예, 옛! 단주의 고강한 무공과 훌륭한 인품에 반해 충성스러운 수하가 되기로 맹세했습니다!”

풍양은 미묘한 얼굴로 코를 긁적였다.

그랬던가? 그가 기억하는 건 서른 명쯤 되는 부하를 데리고 단주랍시고 거들먹거리는 쓰레기를 일 합에 죽인 것뿐이었다.

“내 기억과는 좀 다르지만 어쨌든 고맙네.”

“아닙니다, 영광입니다!”

“그런데 말이야. 토호단은 어땠을지 모르지만, 이곳 적풍단은 좀 달라. 고원의 전통이라든지 하는 자질구레한 것들 말일세.”

“아, 미처 몰랐습니다.”

“단주인 내 명령이 최우선이야. 알겠나?”

“앞으로 명심, 또 명심하겠습니다!”

“아마 저 친구들도 몰라서 고원의 전통을 지킨 모양이야. 다들 자네처럼 새로 합류한 이들이거든. 그러니 가서 내 뜻을 전해 줄 수 있겠나?”

“존명. 한 놈도 살려 두지 않겠습니다.”

마적답지 않게 어설픈 군례까지 갖추는 그를 향해 풍양은 손을 내저었다.

“그래, 어서 가 보게.”

“옛!”

말을 몰아 떠나는 그의 뒷모습을 응시하던 풍양이 돌연 소매를 떨쳤다.

쉭, 바람이 갈라지는 소리와 함께 뻗어 나간 빛줄기가 십 장(약 30m) 밖에서 목표를 관통했다.

푹! 털썩.

말은 계속해서 내달렸다.

이미 숨이 끊긴 주인이 등자에 발이 걸려 지금 이 순간에도 너덜너덜해지고 있다는 사실을 모른 채.

“가서 전해. 포로는 없다고. 다 죽이고 불태우라고.”

“예, 단주님.”

풍양의 수하가 떠나고 얼마 지나지 않아 장원 전체가 화염에 휩싸였다. 금세 타들어 가는 현판(懸板)을 확인한 그의 입가에 슬쩍 웃음이 맺혔다.

항산검문 대동지부.

적풍단이 다시 한번 고원을 넘은 순간이었다.



* * *



넓은 대전.

갑론을박을 벌이던 사람들은 전령의 보고에 숨이 턱 막혔다.

“놈들이 대동을 돌파했습니다!”

“버, 벌써?”

“대동지부는? 경계를 위해 나가 있던 인원들은 어찌 되었나?”

“전멸, 전멸입니다. 대동지부는 잿더미가 되었고 생존자는 한 명도 없습니다.”

“뭣이?”

“혹 소식이 잘못 전해진 건 아닌가? 놈들도 지난번에 큰 타격을 입었을 터인데 어찌 이리 빨리……!”

“다른 마적단을 흡수한 듯합니다. 최소 이백 명, 혹은 그 이상입니다.”

“그 말이 사실인가?”

“예, 틀림없습니다.”

“그, 그럼 도대체 언제쯤 여기까지……?”

“빠르면 하루, 늦어도 이틀 안에 놈들의 공격이 시작될 것으로 예상됩니다.”

“끝장이군.”

누군가의 중얼거림은 이 자리에 모인 대부분의 마음과 크게 다르지 않았다.

열 명 남짓한 그들은 모두 항산검문의 주요 직책을 맡은 중진. 그러나 누구 하나 빠지지 않고 마음속으로는 이미 패배라는 단어를 만지작거리는 중이었다.

“철검대주, 이 싸움 자신 있어?”

“각주씩이나 되는 양반이 왜 나한테 물어? 여기서 무인이 나밖에 없나.”

대항산검문의 대주. 당주, 혹은 각주.

한때는 분명 그 위치에 오르길 간절하게 소망한 적이 있었다. 한때는, 말이다.

‘대항산검문은 얼어 죽을. 이제 와서 승진시켜 주면 뭐 하나, 문파가 이 꼴인데.’

‘가만히 둬도 망할 판국에 마적단까지 와서 난장을 피우는군. 어디 보자, 남아 있는 놈들을 박박 긁어모으면 한 백 명 되려나?’

태원진가와의 전쟁으로 팔 할에 가까운 전력을 상실했다.

공들여 키운 정예 무인들과 풍진강호를 헤쳐 온 노련한 중진들, 무엇보다 문파가 가진 힘을 상징하는 절정 고수들과 금력(金力)의 상실이 가장 뼈아프다.

“제기랄, 문주라도 살아 있었다면.”

일개 낭인으로 시작하여 지금의 항산검문을 키워 낸 이천백. 그의 무공과 수완이라면 이 사태를 뒤집을 수 있을 것이다.

그러나 혈랑검 이천백은 이미 죽고 없다. 그의 핏줄 중 살아남은 이는 오직 한 사람뿐이다.

“이런 상황에 약관도 안 된 어린 계집을 문주라고 모셔야 하다니.”

누군가 홧김에 말을 내뱉은 그 순간.

쾅!

굳게 닫혀 있던 대전의 문이 폭발했다.
```

## Final English reading copy

```markdown
# Chapter 109

A messenger hawk.

I’d heard the Jin Family of Taiyuan had only two of them. They were messenger birds, but difficult to train, so they were used only to deliver important information…

*Who sent it?*

Just as I was about to approach the messenger hawk, Wolhwa called out to me.

“You’d better keep your distance. It’s a very wary bird. If Young Master Jin tries to catch it, it’ll fly away.”

“Ah, could it be?”

“It’s a messenger hawk sent from our sect. It was trained to follow a specific tracking scent.”

Wolhwa pulled a small pouch from her robes and shook it. The messenger hawk cautiously approached and rubbed its beak against it.

In that moment, a Lower District Sect member who had somehow already slipped outside untied the cylinder from the hawk’s ankle.

“Where’s it from?”

“A letter sent yesterday from the Sakju Branch to the Branch Leader.”

“Give it to me.”

Wolhwa accepted the letter and read it. Her expression turned complicated.

It took a while before her tightly closed lips finally parted.

“The Red Wind Band Leader… He’s more than I expected.”

“Is this about the Red Wind Band again?”

Wolhwa gave a small nod and handed me the letter.

There was no reason to refuse when she was telling me to read it. Jin Mukyung and Hyuk Mujin, who had been hesitating nearby, cautiously leaned in as well.



The Red Wind Band is moving south across the plateau. Their numbers are estimated at approximately two hundred.



The short line made its meaning clear.

“They’re planning to attack the Mount Heng Sword Sect again.”

“There’s no doubt about it. This news is already a day old, so they must have narrowed the distance by that much—or more.”

We were currently a day and a half away from the Mount Heng Sword Sect.

As a mounted-bandit group, they would be advancing toward their destination with exceptional mobility.

“Unfortunately, our branch doesn’t have a proper intelligence network in the northern region. The one fortunate thing is…”

Wolhwa’s gaze shifted toward the mounted bandits of the Red Wind Band. They had lost the will to fight long ago, and flinched as they lowered their heads.

“We have valuable sources of information right here. I don’t know whether they have any useful information, though.”

After looking over the mounted bandits, she suddenly pointed at one of them.

“You. Stand up.”

“……M-me?”

The man rose with a thoroughly terrified expression. He was younger than I expected. The youngest and weakest of the mounted bandits, he couldn’t even meet Wolhwa’s gaze.

“How old are you?”

“I-I passed twenty this year.”

“Twenty? You’re young. Then again, being young doesn’t stop someone from becoming a mounted bandit.”

“I’m not a mounted bandit! I only became a wandering martial artist recently, but then they said they’d give me a big cut, so I…”

“Ah, so you’re one of the wandering martial artists the Red Wind Band Leader gathered for the last attack?”

“Y-yes! I’ll tell you everything I know!”

“No, it’s all right.”

“Pardon?”

“You don’t look like you know much anyway. What would be the point? Isn’t that right, Chunsam?”

The Lower District Sect member who had silently played the part of our carriage driver until now.

Instead of answering, he pulled a small knife from his robes and drove it into the young man’s chest.

*Thunk—*

A First Rate martial artist’s fast, precise One Strike split the young man’s heart. He opened and closed his mouth soundlessly before collapsing like a puppet with its strings cut.

*Thud.*

A frigid silence pressed down on the scene. While the mounted bandits stared in horror and fear, Wolhwa’s slender finger moved once more.

“You.”

“I-I’ll talk! I’ll tell you everything! I’ve been with the Red Wind Band for a year…”

“Chunsam.”

*Whoosh! Slash!*

“Grrk… Gurg…”

The mounted bandit staggered backward, making a wet, blood-choked sound. He tried to cover his gaping throat, but couldn’t stop the fountain of blood spraying between his fingers.

“You only need to remember two things.”

From head to toe, Wolhwa was covered in crimson blood. She continued in a dry tone.

“Answer only what you’re asked, and tell the truth exactly as it is.”

“……!”

In mere moments, we learned everything there was to know about the Red Wind Band.



* * *

Once we learned that every second mattered, we abandoned the carriage and each chose a horse. Me, Jin Mukyung, Hyuk Mujin, and Wolhwa.

The Lower District Sect member would take the Five-Colored Ghosts and the surviving mounted bandits to a nearby Lower District Sect branch and report what had happened.

“Was that too cruel?”

Wolhwa asked as she lifted a saddle onto her horse. I scratched my chin.

“To be honest, I was a little surprised.”

I had temporarily forgotten because I had only ever seen her relaxed and playful. She was a martial artist too.

*And an experienced one at that.*

How old was Wolhwa, anyway?

I’d never asked, so I didn’t know for sure, but she couldn’t have been over thirty.

To become the Branch Leader overseeing all of Shanxi at such a young age, she had to possess the decisiveness to match the position.

*Cruel, but effective.*

She had killed two people without hesitation. Just as casually as swatting flies.

Jin Mukyung’s display against the leader must have terrified the mounted bandits, but the fear of death was even greater.

Driven to the edge of a cliff, they had no choice but to pour out information desperately.

“I think I would’ve spilled everything too.”

“I’m saying this in case Young Master Jin gets the wrong idea, but I don’t enjoy killing people. They weren’t innocent commoners, either… Ah, this bastard’s blood just won’t stop, even when I wipe it.”

The blood streaming down her belonged to the second mounted bandit she had killed.

As she wrinkled her nose, someone held out a piece of cloth to her.

“U-use this to wipe it off.”

“Oh my.”

“Huh?”

“Hmm.”

At the reactions from Wolhwa, me, and Hyuk Mujin, Jin Mukyung cleared his throat repeatedly.

“I thought you might need it.”

“Thank you, Young Hero Jin. I needed it.”

“It’s nothing.”

His expression, however, looked quite pleased.

*No way. Is he…*

*The type who’s only nice to women?*

There was always at least one guy like that wherever you went. Even the Heaven Shaking Sword wasn’t any different, apparently.

After wiping away the blood, Wolhwa pulled a rolled-up piece of leather from her robes and spread it out.

“This is a rough map of the entire Shanxi region. Our location is here. The Red Wind Band has probably… If they’ve been moving without rest, they may have already broken through Datong.”

“They’re faster than us.”

“By half a day for now. But the roads along our route are well maintained, so if we ride day and night, we can narrow the gap enough.”

In short, she was telling us not to expect any rest.

I followed the others and leaped onto my saddle.

*Why does something always happen the moment I arrive?*

I wanted to sigh, but what could I do? It wasn’t as though this was my first hardship—or my second. I’d just have to accept it.

*Wasn’t this supposed to be a really simple Quest?*

*Ding.*



> **System**
>
> Quest difficulty has changed to **Peak**.



“……”

Right. I guess it wasn’t simple anymore.



* * *

He was a man who resembled a fox. His pointed chin and ears, along with his sharp, slanted eyes, watched and observed everything around him at once.

“Graaah!”

“Kill them! Kill every last one of them!”

“Aaaah!”

Smoke billowed from a large manor, accompanied by screams.

The man sitting on horseback and gazing down from the hill was Pung Yang, the Red Wind Band Leader. He didn’t speak until the manor had fallen silent.

“Is it over?”

A mounted bandit who had just climbed the hill to deliver his report answered.

“We killed all the men and gathered the women and children together.”

“Why?”

“Pardon? Why, because it’s the plateau’s tradition, of course…”

Any male taller than a cartwheel—even a child—was killed without mercy, while the women were taken or sold as slaves. It was a tradition—or something close to one—passed down from the nomads.

At the mounted bandit’s words, Pung Yang quietly crooked one finger.

“Come closer.”

The mounted bandit approached hesitantly and asked carefully,

“Leader, did I perhaps make some serious mistake…”

“Where did you belong before?”

“Until recently, I was the deputy leader of the Toho Band.”

“The Toho Band? Ah, I remember. You were their deputy leader.”

“Y-yes! I was so impressed by your formidable martial arts and noble character that I swore to become your loyal subordinate!”

Pung Yang scratched his nose with an ambiguous expression.

*Was that so?*

All he remembered was killing a piece of trash in a single strike—the man who had swaggered around calling himself a bandit leader while commanding some thirty subordinates.

“My memory differs a little, but thank you anyway.”

“Not at all! It’s an honor!”

“However, the Earth Tiger Band may have been different. The Red Wind Band has its own way. Those petty matters about plateau traditions, for example.”

“Ah, I didn’t realize.”

“My orders as leader take priority. Do you understand?”

“I’ll keep that in mind—over and over again!”

“Those fellows probably followed the plateau’s traditions because they didn’t know any better. They all joined recently, just like you. So go and convey my wishes to them, will you?”

“Understood. I won’t leave a single one alive.”

The mounted bandit even gave an awkward military salute, though there was nothing military about a mounted bandit. Pung Yang waved him away.

“Yes, go on.”

“Yes, Leader!”

Pung Yang watched him ride away, then suddenly flicked his sleeve.

With a sharp sound as the air split, a streak of light shot out and pierced its target ten jang away—about thirty meters.

*Thud!*

*Clatter.*

The horse continued racing forward.

Its rider was already dead, but his foot remained caught in the stirrup. Unaware that his body was being dragged and battered to shreds, the horse galloped on.

“Go and tell them. There are no prisoners. Kill them all and burn the place.”

“Yes, Leader.”

Not long after Pung Yang’s subordinate departed, the entire manor was engulfed in flames. As he watched the signboard burn away in an instant, a faint smile touched the corners of his mouth.

The Datong Branch of the Mount Heng Sword Sect.

The moment the Red Wind Band crossed the plateau once more.



* * *

The people gathered in the spacious main hall had been arguing back and forth when the messenger’s report left them speechless.

“They’ve broken through Datong!”

“A-already?”

“What about the Datong Branch? What happened to the men who went out to stand guard?”

“Everyone was wiped out. Everyone. The Datong Branch was reduced to ashes, and there were no survivors.”

“What?”

“Could the report be wrong? They must have suffered heavy losses last time, so how could they have come this far so quickly…?”

“They appear to have absorbed another mounted-bandit group. At least two hundred men—possibly more.”

“Is that certain?”

“Yes, without a doubt.”

“Th-then when will they reach us…?”

“If they’re fast, the attack will begin within a day. At the latest, we expect it within two days.”

“We’re finished.”

The muttered words were not much different from what most of the people gathered there were thinking.

There were a little over ten of them, all senior figures holding important positions in the Mount Heng Sword Sect. Yet every one of them was already turning the word *defeat* over in their minds.

“Iron Sword Squad Leader, are you confident in this fight?”

“Why are you asking me, when you’re a Pavilion Leader? Am I the only martial artist here?”

They were squad leaders, hall leaders, and pavilion leaders of the great Mount Heng Sword Sect.

There had been a time when he had desperately wanted to rise to that position. Once upon a time, that was.

*To hell with being a commander of the Mount Heng Sword Sect. What good is a promotion now, with the sect in this state?*

*We were already doomed if left alone, and now a mounted-bandit group has come to make a mess of everything. Let’s see… If we scrape together every man we have left, there might be a hundred of them.*

The war with the Jin Family of Taiyuan had cost them nearly eighty percent of their strength.

The loss of the elite martial artists they had painstakingly trained and the seasoned senior figures who had weathered the martial world was painful enough. Most devastating of all was the loss of the Peak masters who represented the sect’s power—and its financial resources.

“Damn it. If only the Sect Leader were still alive.”

Lee Cheonbaek had started as a mere wandering martial artist and built the Mount Heng Sword Sect into what it was now. With his martial arts and resourcefulness, he could have turned this situation around.

But the Blood Wolf Sword, Lee Cheonbaek, was already dead. Of his bloodline, only one person remained alive.

“To think we have to serve some little girl who isn’t even twenty as Sect Leader at a time like this.”

At that moment, someone spat out the words in a fit of anger.

*Boom!*

The tightly closed doors of the main hall exploded.
```
