<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0134.txt",
      "sha256": "afdc1572660366eda3c3b6112941957d9766e7b4559e656bf1d8a68692815ce2",
      "bytes": 13186
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "f0a065bf6ec1b2f30a39b3be7a1558b53e0cbca0770a5e468f49a8b8eff7c00f",
      "bytes": 7829
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "fee9dc401014e2e645c751e2e2f57d17fe7a745691859b626c29a43675ec865d",
      "bytes": 26278
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "a8406fab04cdea1b94ef7c155cd67f921109988b6e80fcd762fa4ed9b4926354",
      "bytes": 719
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fdf92d16a166b9e04b05ce236c96c9fe7d8203f7c2a63af7a35e60404c59c9d7",
      "bytes": 5353
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1007cf44da9263848260eaf9f6e0440199d935c5e5e26b860e76e161e54bab9e",
      "bytes": 24583
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "677b60575be861f87037a1d8d8d8675914fde6ea5e08d825697b0db7811bdfbd",
      "bytes": 622
    },
    {
      "path": "characters/Woo Jintae.md",
      "sha256": "16c65d4d217ec305e22dff98ce46416a100f195330fc4dee4a98ab3d3c40fab7",
      "bytes": 745
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "797c581cb9ae2051d772c1392f55c948f5ae83f96a784d94825ab2c8e7c93c5d",
      "bytes": 22012
    }
  ],
  "estimated_tokens": 23277
}
-->

# Durable State Update — Chapter 134

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 134. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 134. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 134,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 134,
    "continuity_sources": [134],
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
    "Pung Yang is dead; Jin Taekyung killed him after the Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed his Body-Protecting Qi and pierced his chest.",
    "Taekyung fully absorbed the Blazing Flame Divine Pill and possesses forty-five years of internal energy with the Scorching Yang Qi attribute.",
    "Jin Mukyung survived his fight with Pung Yang and returned to the Jin Family of Taiyuan, but remains incompletely recovered.",
    "Cheol Mubaek remains severely injured and needs extended recuperation; Lee Seowol remains the seventeen-year-old Sect Leader of the Mount Heng Sword Sect and vows to preserve it.",
    "The Lower District Sect sent a relief force after the battle; Wolhwa's real name is Eun Sowol, and she is its Shanxi Branch Leader.",
    "Lee Seowol accepted the Jin Family of Taiyuan's New Year invitation, offered the Mount Heng Sword Sect's territorial rights as an apology, and proposed marriage to Taekyung in exchange for three Peak martial arts; Taekyung plans to reject her because of her age and because he loves Song Song.",
    "Forty-seven mounted bandits survived the battle, but the Lower District Sect can save only about thirty; it is spreading a rumor that the two Jin brothers defeated Pung Yang and rescued Mount Heng.",
    "Cheol Mubaek and Lee Cheonbaek became close friends after first meeting and fighting more than thirty years ago; Cheol is the ninth-generation successor of the Shura Annihilating Fist.",
    "Jopil is dead and left behind the Supreme Peak martial art Flame Divine Palm; the Fire King and the status of the Fire Gate Clan's single successor remain unknown.",
    "The Temporary Strength Pill is in Taekyung's Inventory and has been revealed to Jin Wikyung, Jin Mukyung, and Wipeng; its System description identifies Dark Heaven as its manufacturer and records its unknown Grade, Peak restriction, temporary power increase, +100 combat stats, fifteen years of internal energy, and Body-Protecting Qi effect.",
    "Jin Wikyung and Wipeng traveled to Sakju with fifty elite guards after receiving an emergency report about Pung Yang, the Red Wind Band, the Mount Heng Sword Sect, and the Jin brothers; the Jin Family displayed a large Sakju banner celebrating the safe return of Mukyung, Taekyung, and Hyuk Mujin.",
    "Taekyung, Mukyung, Wikyung, and Wipeng drank through the night for three days; Wipeng is called the God of Drinking and Taekyung is rumored to be the Night King.",
    "Taekyung's Sleeping Dragon of Shanxi Title effect strengthened to all stats +15 and Fame +200; his current Status Window shows Level 61, Fame 2,100 (+250), and 60 remaining points.",
    "Hyuk Mujin accepted The City Lord's Invitation, requiring attendance at the City Lord's luncheon with young prodigies tomorrow.",
    "The City Lord of Shanxi Province is a ten-year-old Prince and the Emperor's youngest brother, appointed at age five; Jin Mukyung met him after being summoned three years earlier and considered the encounter a nightmare.",
    "Cheongpung is an eccentric former porter who recently fled Huashan's Lotus Peak and traveled toward Taiyuan; he is an exceptionally young Peak master whose Level Taekyung cannot determine through Qi Sense, lived with his grandfather in the mountains from age five, and came down to test himself against the Ten Dragons and Phoenixes.",
    "Hyuk Mujin's parents are healthy textile merchants in Taiyuan who own the city's largest textile shop, with branches in Henan and Hebei; Mujin left home to avoid inheriting the business, and a younger sibling later removed that obligation.",
    "Taekyung has begun treating Hyuk Mujin as a valued companion rather than merely a subordinate, acknowledging the hardship Mujin endured while traveling with him.",
    "Woo Jintae is the heir of the Seongun Escort Bureau and cultivates the current Five Gates of Shanxi's scions through lavish hospitality, gifts, and bribes.",
    "The five young prodigies who mocked Taekyung, Mujin, and Cheongpung at Honghwa Inn are Seongryong, Cheonwoo, Myeonghwa, Sohye, and Jintae; they are pampered First Rate scions, and Jintae is Level 45."
  ],
  "continuity_sources": [
    133,
    132
  ],
  "open_questions": [
    "How will the Jin Family of Taiyuan respond to Lee Seowol's proposed transaction and territorial transfer?",
    "Can Lee Seowol preserve or rebuild the Mount Heng Sword Sect with so few survivors?",
    "What are the Temporary Strength Pill's exact price and long-term aftereffect, and is it related to the Demonic Cult's Blood-Exploding Pill?",
    "What is Dark Heaven, and why do Jin Wikyung and Wipeng refuse to discuss it?",
    "What consequences will Pung Yang's death have for the Red Wind Band and the wider Murim?",
    "Is the Fire King still alive, and if so, where is he?",
    "What will happen at the City Lord's luncheon and how will the City Lord react to Taekyung?",
    "What was Cheongpung's status at Huashan's Lotus Peak, who is his grandfather, and what are the individual sect affiliations or family names of the five current Five Gates scions? "
  ],
  "safe_through": 133,
  "temporary_decisions": [
    "Render 잠력단 as Temporary Strength Pill and 폭혈단 as Blood-Exploding Pill.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron and 이름 없는 검 as Unnamed Sword.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years of internal energy.",
    "Render 완전 회복 as Full Recovery and 회광반조 as final rally in this death-and-recovery context.",
    "Render 운칠기삼 as seven parts luck and three parts skill, and 운구기일 as nine parts luck and one part qi, with a footnote explaining the variation.",
    "Render 은공 as Benefactor, 절정 무공 as Peak martial arts, 급식 as school lunch, 고딩 as high schooler, 철컹 as clank, 산서성 as Shanxi Province, 총지부장 as Chief Branch Leader, 원단 as New Year's Day, 갑자 as jiazi, 시진 as shichen, 표행 as escort run, 쟁자수 as porter, 표국 as Escort Bureau, 표두 as Escort Chief, 은원보 as silver ingot, 은자 as nyang of silver, 사서삼경 as the Four Books and Three Classics, and 연화봉 as Lotus Peak.",
    "Render 일인전승 as single successor, 비인부전 as transmission only to the worthy, 구 대 계승자 as ninth-generation successor, 천하십대권법 as the ten greatest fist techniques in the world, 열화문 as Fire Gate Clan, 화왕 as Fire King, 삼성 as Three Saints, 십왕 as Ten Kings, 진무보법 as Jin Family's Manoeuvre Technique, 아이템창 as Item Window, 전서응 as messenger eagle, 고원 as Gaoyuan, 구주 as Nine Provinces, 사술 as dark arts, 마기 as demonic qi, 선천지기 as innate qi, 소음인 as Soeumin, 태양인 as Taeyangin, 암천 as Dark Heaven, 주신 as God of Drinking, 야왕 as Night King, 화주 as fire liquor, 화북 as North China, 현령 as county magistrate, 성주 as City Lord, 장 노인 as Old Man Jang, 적토마 as Red Hare, 여포 as Lü Bu, 성주의 초청 as The City Lord's Invitation, 친왕 as Prince, 주씨 as Zhu, 천자 as Son of Heaven, 황상 and 황제 as Emperor, 태자 as Crown Prince, 구파일방 as Nine Sects and One Gang, and 오대세가 as Five Great Families; render 개방 as Beggars' Sect and 십봉룡 as Ten Dragons and Phoenixes.",
    "Render 빙당호로 as candied hawthorn skewers with an explanatory footnote; render 산니백육 as Garlic Pork, 어향육사 as Fish-Fragrant Shredded Pork, 경장육사 as Beijing Sauce Shredded Pork, 규화계 as Beggar's Chicken, 매구 as Maegu, 매채구육 as Maechae Guyuk with a footnote explaining the abbreviation, 촉금 as Shu brocade, 삼도문 as Samdo Sect, and 궁귀문 as Gunggui Sect."
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
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |

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
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 혁무진    | **Hyuk Mujin**     |
| 청풍     | **Cheongpung**     |
| 태원진가   | **Jin Family of Taiyuan**        |
| 산서오문   | **Five Gates of Shanxi**         |
| 일류     | **First Rate**    |
| 무인     | **martial artist**                               | Default term                                          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 경지     | **realm** / **realm stage**                      | Especially power level                                |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 보법     | **manoeuvre technique** / **footwork technique** | Named Jin technique uses “Manoeuvre”                  |
| 영약     | **elixir**                                       |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 중원     | **Central Plains**                               |                                                       |
| 표국     | **Escort Bureau**                            |
| 소국주    | **Young Bureau Head**                        |
| 제자     | **Disciple**                                 |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 하남     | **Henan**              |
| 귀가      | **your family**                                                 |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 133
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Raised by his grandfather in the mountains from age five; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 133
- **Aliases:** None revealed
- **Role:** First Rate martial artist from a wealthy Taiyuan textile-merchant family; Captain of the Gatekeepers at the Jin Family of Taiyuan; deputy squad leader of White Tiger Hall’s reconnaissance squad; candidate to become the next Master of the Gatekeeper Pavilion; traveling as Jin Taekyung’s attendant for the City Lord’s luncheon
- **Personality:** Young, disciplined, suspicious of Jin Taekyung, and openly contemptuous of the family’s disgraced third son; believes loyalty and respectable conduct matter, but is also proud and hungry for glory
- **Voice:** Formal and clipped when performing his duties; blunt and moralizing when addressing Taekyung
- **Relationships:** Gatekeeper under the Jin Family; deputy subordinate to Jin Taekyung in the reconnaissance squad; son of the Hyuk Family Textile Shop’s owners, with a younger sibling who removed the need for him to inherit the family business

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 132
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm who now possesses forty-five years of internal energy with the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 61 with 2,100 Fame and 60 unspent stat points, and the Sleeping Dragon of Shanxi Title now grants all stats +15 and Fame +200
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 133
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Woo Jintae.md

# Woo Jintae (우진태)

- **Safe through:** Chapter 133
- **Aliases:** None
- **Role:** Heir of the Seongun Escort Bureau and a leading scion of the current Five Gates of Shanxi; hosts its young members at Honghwa Inn and prepares for the City Lord's luncheon.
- **Personality:** Boastful, calculating, status-conscious, and manipulative; treats lavish gifts and money as tools for creating obligations.
- **Voice:** Charming and lavish in public, with polished courtesy that turns dry and contemptuous when he judges someone beneath him.
- **Relationships:** Heir to the Seongun Escort Bureau; cultivates the current Five Gates scions through hospitality, gifts, and bribes.

## Korean source

```text
＃134화



쫙!

찰진 소리와 함께 우진태의 고개가 옆으로 돌아갔다. 그는 멍하니 자신의 뺨을 쓰다듬었다.

‘지금 무슨 일이 벌어진 거지?’

어안이 벙벙하다. 따귀를 맞아? 내가 고작 이런 놈한테?

내일모레면 이립(而立)인 그는 일찍 혼사를 치른 덕분에 이미 가정도 있었다.

그런데 약관이나 됐을까 싶은 어린놈한테 이런 치욕을 당하다니.

“꺄악! 우 소협!”

“혀, 형님, 괜찮으십니까?”

“저거, 저거 성운표국의 소국주 아녀?”

“맞네. 세상에, 어떤 간 큰 놈이…… 가만, 어디서 본 얼굴 같은데?”

뒤늦은 후기지수들의 반응과 객잔 손님들의 시선이 우진태의 수치심을 배로 키웠다.

그는 살기 어린 눈빛으로 눈앞의 애새끼를 노려봤다.

“네놈이 감히…….”

“그게 아니지.”

“뭐?”

“감히, 가 아니라 어떻게, 가 나와야 하는 거야. 네가 무인이라면.”

우진태가 순간 멈칫했다. 어릴 적부터 성운표국의 전폭적인 지원 아래 각종 영약과 일류 무공을 흡수한 그다.

그러니 뛰어난 무재를 타고나진 않았어도 여타 후기지수에 비해 일초반식은 앞선다고 자부하는 것도 당연했다.

‘그런 내가 이렇게 쉽게 당해?’

놈이 언제, 어떻게 다가왔는지 제대로 보지도 못했다. 사람들 앞에서 개망신을 당했다는 사실에 치욕감이 앞섰을 뿐이다.

우진태는 그제야 경계심이 가득한 눈으로 상대방을 훑었다.

“이 자식 눈깔 굴리는 것 보게. 왜, 쓰리 사이즈 알려 줘?”

“어느 문파의 누구냐?”

“도동파의 천진반이다, 이 새끼야.”

어린놈의 욕설을 참을 수 있었던 것은 이성이 돌아왔기 때문이었다.

무림에서는 무슨 일이 일어날지 모르는 법. 만약 상대가 대문파의 제자라면 깔끔하게 물러나야 한다.

‘도동파, 도동파의 천진반이라고?’

문파도, 놈의 이름도 생소하기 짝이 없다. 슬쩍 뒤를 돌아보니 다른 후기지수들의 얼굴에도 어리둥절한 기색이 역력하다.

우진태의 머리가 팽팽 돌아갔다.

‘내가 알기로 산서성에 도동파라는 문파는 없다.’

이미 각 문파들이 확고히 자리를 잡은 산서성에서 개파(開派)를 한다는 건 불가능에 가깝다.

다른 문파들의 견제는 둘째 치더라도 금세 소문이 날 수밖에 없는 구조다.

‘저 나이에 이만한 경지의 후기지수를 키워 냈다면 상당한 역량의 문파라는 건데……. 어디지? 섬서 쪽인가? 아니면 하남?’

우진태가 쉽게 입을 열지 못하고 눈만 뒤룩뒤룩 굴리던 그 순간이었다.

멀뚱멀뚱, 강 건너 불구경만 하고 있던 젊은 무인이 불쑥 물었다.

“도동파는 또 뭡니까? 진짜 있는 문파예요?”

“있겠냐? 원래 거짓말도 그럴듯하게 치면 실화가 되는 법이란다.”

“아하. 금과옥조 같은 말씀, 가슴에 새기겠습니다.”

“짜식, 오랜만에 말 예쁘게 하네.”

거지처럼 남루한 옷차림의 청년도 한마디 보탰다.

“거짓말도 잘 치면 실화다…… 좋은 말씀입니다. 현기(玄機)가 느껴져요.”

“……아, 예. 일단 칭찬은 고맙네요.”

세 사람의 대화를 들은 우진태의 눈에서 불똥이 튀었다.

“놈! 정체를 밝혀라!”

“왜, 어디의 누구인지 들어 본 다음 만만하면 한판 붙고 급이 좀 높다 싶으면 꼬리 말고 사과하게?”

“…….”

적나라하지만 정곡을 찌르는 한마디다. 쉽게 입을 떼지 못하는 우진태를 보며 어린놈이 끌끌 혀를 찼다.

“인마, 넌 질문부터가 글러 먹었어. 방귀 뀐 놈이 성낸다더니, 내 대답을 듣고 싶었으면 먼저 사과부터 했어야지.”

우진태는 지그시 입술을 깨물었다.

사과?

성운표국의 삼대독자로 태어나 평생을 떠받들어져 살아온 그다. 어디 출신인지도 모를 상대에게 머리를 숙일 만큼 유연한 사고방식의 소유자가 아니었다.

마침내 결심한 우진태는 산서오문의 후기지수들을 향해 은밀히 눈짓했다.

‘저놈이 아무리 강해 봤자지.’

상대는 고작 셋. 반면 이쪽은 산서성에서 손꼽히는 후기지수들로 이루어진 일류 고수 다섯이다.

자신의 신호에 슬쩍 병장기를 움켜잡는 네 남녀를 보니 마음이 든든해진다.

“내가, 아니 우리가 누군지는 알고 있나?”

“어쩌다 보니 이름 석 자 정도는. 그런데 그게 사과냐?”

“사과? 간도 크군.”

우진태가 비릿하게 웃었다.

“우리는 산서오문의 후계자들이다. 산서오문을 모른다고 하지는 않겠지.”

“안다고 해 줄게. 근데 진짜 사과 안 해? 이거 마지막 경고야.”

“나도 경고하지. 어디에서 온 놈인지는 몰라도 사람 잘못 건드렸…….”

쫙!

우진태의 눈앞이 번쩍했다. 저도 모르게 뒷걸음질 치는 그에게 번개 같은 싸대기가 연이어 작렬했다.

쫙! 쫙! 쫘좍!

한 걸음에 한 대씩. 도합 다섯 대를 맞은 우진태가 비틀거렸다.

집요할 정도로 한쪽만 때린 탓에 뺨은 퉁퉁 부어올랐고, 터져 나간 입 안엔 핏물이 고였다.

‘아버지에게도 맞아 본 적이 없는데.’

난생처음 겪는 수모. 그것도 만인이 보는 앞에서 벌어진 일이다.

그의 눈이 희번덕거렸다.

“이런 개……!”

“말했지, 마지막 경고라고. 혹시 마지막이라는 뜻을 모르는 거냐, 아니면 경고의 뜻을 모르는 거냐? 아니면 둘 다?”

“감히 날 쳐?”

“널 함부로 대한 남자는 내가 처음이겠지만 제발 사랑하진 말아라. 난 송이 씨 한 명 사랑하는 것도 바빠.”

“죽인다!”

“때린다!”

쫙쫙쫙!

“커헉!”

우진태는 정신을 차릴 수 없었다.

공력이 실린 것도 아니요, 그렇다고 신묘한 보법을 밟는 것 같지도 않다. 그런데도 한쪽도 아니고 두 뺨을 향해 쏟아지는 따귀 세례를 도저히 막을 방법이 없었다.

‘이게 어떻게 된 일이란 말이냐!’

속수무책으로 당하고 있는 그의 귓가에 광기 어린 외침이 파고들었다.

“왼손으로 때리고, 오른손으로 때리고!”

쫙쫙!

“한치 두치 세치 네치 뿌꾸 뺨! 뿌꾸 뺨!”

쫙쫙쫙!

끊임없이 알아들을 수 없는 말을 외치면서 따귀를 날리는데, 그 모습이 꼭 따귀를 때리기 위해 태어난 미친놈 같았다.

바로 지금처럼.

“왼손 올리고 오른손 내려. 오른손 내리고 왼손 내려. 왼손 내리고 오른손 올리지 마.”

“허억!”

“옳지. 잘했어요. 선생님이 상으로 우리 우진태 어린이의 뺨을 호되게 때려 줄 거예요.”

쫙쫙쫙쫙!

불과 촌각도 되지 않는 시간 동안 얼마나 맞았을까. 삼십 대? 오십 대?

하도 정신없이 맞았더니 머리가 띵하고, 눈에는 눈물이 핑 돈다.

결국, 우진태가 할 수 있는 것은 구조 요청뿐이었다.

“나, 나 좀 도와주시오!”



* * *



성운표국. 재력으로만 따지면 산서 제일의 태원진가에도 비견할 만하다는 바로 그 성운표국의 소국주가 간절한 목소리로 외친다.

“제, 제발 도와주시오!”

자존심이고 뭐고 전부 내팽개친 절박한 음성에도 산서오문의 후기지수들은 쉽사리 병장기를 뽑지 못했다.

“저걸 어떻게 이겨…….”

누군가가 신음처럼 흘린 말은 모두의 마음을 대변하는 것이었다.

맞다. 직접 겪어 볼 필요도 없다.

옆에서 보는 것만으로도 오금이 저리고 다리가 풀릴 정도였다. 상대는 자신들과 나이만 엇비슷할 뿐, 상상을 뛰어넘는 고수임이 틀림없었다.

“저 나이에 이 정도 경지라니.”

“저건 완전 괴물이잖아.”

쫙쫙!

“사, 살려 주시오!”

한층 더 절박해진 목소리. 구조 요청도 미묘하게 변했다.

이대로 조금만 더 지난다면 차라리 죽여 달라는 말이 나올지도 모르겠다.

“도, 도와야겠죠?”

“최소한 말리기라도 해야…… 왕 공자가 어떻게 좀 해 봐요.”

“저요? 갑자기 저는 왜요?”

“왜긴요. 모일 때마다 가전무공 자랑했잖아요. 중원 어디에 내놔도 부끄럽지 않은 검공(劍功)이라면서요?”

평소 틈만 나면 가전무공의 위대함을 자랑했던 왕가장의 후계자가 정색하고 대답했다.

“저는 도객이라 검공 안 익혔습니다.”

“네?”

“그리고 그걸 왜 나한테 떠넘깁니까? 정 말리고 싶으면 신 소저께서 나서시면 될 것 아닙니까?”

“어머. 별꼴이네, 진짜.”

산서오문의 후기지수들이 서로에게 차례를 미루던 그때, 가만히 상황을 지켜보던 혁무진이 불쑥 끼어들었다.

“쓸데없는 고민들 하시네. 나 같았으면 얼른 가서 한 손이라도 보탰소.”

“네놈, 아니 당신은 뭐요?”

워낙 무서운 광경이 눈앞에서 펼쳐지고 있으니 별것 아닌 무인 하나에게도 반존대를 써야 했다.

불과 일각 전 우진태에게 촉금을 선물로 받았던 황 소저도 재빨리 나섰다.

“미리 말해 두는데, 우리는 당신들한테 아무런 악감정이 없어요. 알죠?”

“그래요? 정 그렇다면 뭐, 그렇다고 칩시다.”

“그렇다고 치는 게 아니라 사실이 그렇다는 말이에요.”

“그걸 나한테 말해 봤자 무슨 소용이겠습니까?”

혁무진이 실실 웃으며 우진태를 신명 나게 두들겨 패고 있는 진태경의 뒷모습을 턱짓으로 가리켰다.

“우리 조장님이 한 성깔 하시거든요. 저기 신명 나게 맞고 있는 분이 쓰러지면 다음 차례는 누가 될까…… 거기 공자님? 아니면 옆에 계신 소저?”

“…….”

“아, 혹시나 해서 말해 두는데 저 양반은 남녀 구분 없이 다 때립니다.”

“나, 난 안 웃었소!”

“저도 마찬가지예요!”

“똑같은 말 두 번 해야 합니까? 나한테 말해도 소용없다니까요. 아, 그나마 가능성이 있는 방법이 하나 있긴 하네.”

“방법?”

후기지수들의 귀가 번쩍 뜨였다.

다들 그동안 무공을 아주 공으로 익힌 것은 아닌지라, 저 괴물 같은 청년을 상대로는 승산이 없음을 깨닫고 있었다.

“사, 사람 살려…….”

때마침 귓가로 흘러 들어온 우진태의 죽어 가는 목소리는 생존 본능에 더욱 불을 지폈다.

“그, 그 방법이란 게 도대체 뭐요?”

혁무진이 짐짓 심각한 얼굴로 턱을 쓸었다.

“글쎄, 이거 하나같이 방귀깨나 뀌는 집 자제분들이라 할 수 있으실지 모르겠는데.”

“하겠소!”

“할게요! 무조건 할게요!”

“음. 기본이 됐군요.”

흡족한 얼굴로 고개를 끄덕인 혁무진이 입을 헤 벌린 채 일방적인 구타를 구경하던 청풍을 가리켰다.

“우선 여기 계신 이분께 정중히 사과할 것.”

말이 끝나기가 무섭게 산서오문의 자제들이 허리를 접었다.

“진심으로 사과드리겠소.”

“겉모습만 보고 섣부른 판단을 했던 점. 정말 죄송스럽게 생각해요.”

청풍이 뒤통수를 긁적였다.

“전 괜찮으니 다들 일어나세요.”

앞서 많은 사람 앞에서 비웃음을 당한 것 치고는 너무 흔쾌히 용서해 주어 되레 혁무진이 당황했다.

심지어 불쾌함에 응당 붉어져 있어야 할 안색은 해맑기까지 했다.

“이렇게 쉽게 말입니까?”

“네. 무슨 문제라도 있나요?”

“그건 아니지만…… 아까 화나시지 않았습니까? 이렇게 공공연한 장소에서 모욕을 당하셨는데.”

“화가 왜 나요? 그냥 좀 신기한데.”

“예? 그게 무슨.”

“아까처럼 많은 사람이 저를 주목한 건 처음이었거든요. 절 무시한 사람한테 사과받는 것도 처음이라 신기하고 재밌던데요.”

“…….”

“아, 역시 하산하길 잘한 것 같아요.”

이놈도 살짝 맛이 갔구나.

해괴한 사람을 보는 듯한 눈빛으로 청풍을 바라보던 혁무진이 고개를 절레절레 저으며 후기지수들을 바라봤다.

“들으셨죠? 여기 계신 소협께서 사과를 받으셨으니 이 문제는 여기서 마무리 짓겠습니다.”

“오오!”

“오오오, 살았다!”

그러나 혁무진의 말은 거기서 끝나지 않았다.

“자, 그럼 마지막 두 번째가 남았습니다.”

“……두 번째라니?”

“더 있어요?”

“네, 이게 가장 중요합니다.”

이윽고, 그가 자신을 바라보는 네 남녀를 향해 엄숙하게 선언했다.

“다들 대가리 박으십쇼.”

“……!”

“……!”
```

## Final English reading copy

```markdown
# Chapter 134

*Smack!*

Woo Jintae’s head snapped to the side with a satisfyingly solid sound. He blankly stroked his cheek.

*What just happened?*

He was dumbfounded.

Had he just been slapped? By a punk like this?

Woo Jintae was nearing thirty. Thanks to marrying young, he already had a family of his own.

And now he had suffered this humiliation at the hands of some kid who couldn’t have been more than twenty.

“Eek! Young Hero Woo!”

“H-Hyung, are you all right?”

“Isn’t that the Young Bureau Head of the Seongun Escort Bureau?”

“That’s him. My goodness, what kind of reckless bastard would… Wait. Doesn’t that face look familiar?”

The belated reactions of the young prodigies and the stares of the inn’s guests doubled Woo Jintae’s shame.

He glared at the little bastard in front of him with eyes full of killing intent.

“How dare you…”

“That’s not the right way to put it.”

“What?”

“Not *how dare you*. You should be asking *how did you do that?* If you’re a martial artist.”

Woo Jintae froze for a moment.

Since childhood, he had received the full support of the Seongun Escort Bureau, taking in all kinds of elixirs and First Rate martial arts. Even if he hadn’t been born with extraordinary talent, it was only natural that he took pride in being a move and a half ahead of the other young prodigies.

*How did I get beaten so easily?*

He hadn’t even seen when or how the bastard approached him. All he had felt was the humiliation of being utterly disgraced in front of everyone.

Only then did Woo Jintae study his opponent with eyes full of caution.

“Look at those eyes darting around. What, do you want me to tell you my three measurements?”

“Which sect are you from, and who are you?”

“I’m Tien Shinhan of the Dodong Sect, you son of a bitch.”

The only reason Woo Jintae managed to endure the young bastard’s profanity was that his reason had finally returned.

In the Murim, you never knew what might happen. If the other man was a disciple of a great sect, Woo Jintae would have to withdraw cleanly.

*The Dodong Sect? The Dodong Sect’s Tien Shinhan?*

Both the sect and the man’s name were utterly unfamiliar. Woo Jintae glanced back. The other young prodigies wore equally bewildered expressions.

His mind began racing.

*As far as I know, there’s no such sect as the Dodong Sect in Shanxi Province.*

Opening a new sect in Shanxi Province, where all the established sects had already secured their positions, was nearly impossible.

Even without interference from the other sects, word would spread immediately.

*If they raised a young prodigy of this level at that age, they must be a sect with considerable power… Where are they from? Shaanxi? Henan?*

That was when the young martial artist who had been standing idly by as though none of this concerned him suddenly asked,

“What’s the Dodong Sect? Is it a real sect?”

“Would it be? A well-told lie becomes fact before you know it.”

“Ah. I’ll engrave those golden words in my heart.”

“You little punk. You’re speaking nicely for once.”

A young man dressed in rags like a beggar added his own comment.

“A well-told lie becomes fact… Those are wise words. I can sense profound wisdom in them.”

“Ah… yes. Thank you for the compliment, at least.”

Sparks flew from Woo Jintae’s eyes as he listened to the three of them.

“You bastard! Reveal your identity!”

“What, you want to hear who I am and where I’m from, then pick a fight if I seem easy and tuck your tail between your legs and apologize if I turn out to be too high-status?”

“…”

It was a crude statement, but it struck the bull’s-eye. Seeing Woo Jintae unable to answer, the young bastard clicked his tongue.

“Punk, you started with the wrong question. They say the one who farted gets angry. If you wanted an answer from me, you should’ve apologized first.”

Woo Jintae bit down on his lip.

An apology?

Born the sole male heir the Seongun Escort Bureau’s family had produced in three generations, he had been pampered and revered his entire life. He wasn’t flexible enough to bow his head to some nobody whose origins he didn’t even know.

At last, Woo Jintae made up his mind and gave the young prodigies of the Five Gates of Shanxi a subtle signal with his eyes.

*No matter how strong he is, he can’t be that strong.*

There were only three opponents. On their side were five First Rate masters, all among Shanxi Province’s foremost young prodigies.

Seeing the four men and women discreetly gripping their weapons in response to his signal, Woo Jintae felt reassured.

“Do you know who I am—or rather, who we are?”

“I happen to know your names, at least. But is that an apology?”

“An apology? You’ve got some nerve.”

Woo Jintae gave a thin smile.

“We are the heirs of the Five Gates of Shanxi. Surely you can’t claim not to know the Five Gates of Shanxi.”

“I’ll say I know. But are you really not going to apologize? This is your final warning.”

“I’ll give you a warning, too. I don’t know where you came from, but you picked the wrong person to mess with—”

*Smack!*

Woo Jintae’s vision flashed white.

As he instinctively stumbled backward, lightning-fast slaps struck him one after another.

*Smack! Smack! Smack-smack!*

One slap with every step.

After taking five slaps in all, Woo Jintae staggered unsteadily.

Because the blows had relentlessly targeted one side, his cheek had swollen grotesquely. Blood pooled inside his split mouth.

*Even my father never hit me.*

It was the first humiliation of his life—and it had happened in front of everyone.

His eyes rolled wildly.

“You fucking—!”

“I told you, final warning. Do you not know what *final* means, or what *warning* means? Or both?”

“How dare you hit me?”

“I may be the first man ever to treat you so casually, but please don’t fall in love with me. I’m busy enough loving one Song-i.”

“I’ll kill you!”

“I’ll beat you!”

*Smack-smack-smack!*

“Guh!”

Woo Jintae couldn’t regain his senses.

There was no internal energy behind the blows, nor did his opponent seem to be using any mystical manoeuvre technique. And yet Woo Jintae had no way to block the storm of slaps raining down on both his cheeks.

*How is this happening?*

As he was beaten helplessly, a crazed shout rang in his ears.

“Slap with the left hand, slap with the right hand!”

*Smack-smack!*

“One chi, two chi, three chi, four chi—Ppukku cheek! Ppukku cheek!”

*Smack-smack-smack!*

He kept shouting words that made no sense while flinging slap after slap. He looked like a madman born for the sole purpose of smacking people across the face.

Just like right now.

“Raise your left hand and lower your right. Lower your right and lower your left. Lower your left, and don’t raise your right.”

“Hurk!”

“That’s right. Good job. As a reward, your teacher will give little Woo Jintae’s cheeks a thorough beating.”

*Smack-smack-smack-smack!*

How many times had he been struck in the space of less than a moment?

Thirty? Fifty?

He had been hit so frantically that his head rang and tears swam in his eyes.

In the end, all Woo Jintae could do was call for help.

“P-please! Somebody help me!”

* * *

The Young Bureau Head of the Seongun Escort Bureau—the very Seongun Escort Bureau whose wealth alone was said to rival that of the Jin Family of Taiyuan, the richest family in Shanxi—cried out in desperation.

“P-please help me!”

Having thrown away his pride and everything else, Woo Jintae’s desperate plea still failed to make the young prodigies of the Five Gates of Shanxi draw their weapons.

“How are we supposed to beat that…?”

Someone’s groan spoke for everyone.

They were right. There was no need to experience it firsthand.

Just watching from the side was enough to make their knees go weak and their legs tremble. Their opponent was roughly the same age as them, but there was no question that he was a master far beyond their imagination.

“To reach that realm at his age…”

“That thing’s a complete monster.”

*Smack-smack!*

“P-please spare my life!”

Woo Jintae’s voice grew even more desperate. Even his plea for help had subtly changed.

If this continued much longer, he might start begging them to kill him instead.

“We, we should help him, right?”

“At the very least, we should try to stop him… Young Master Wang, do something.”

“Me? Why am I suddenly involved?”

“Why do you think? Every time we got together, you bragged about your family’s martial arts. You said it was sword arts you could display anywhere in the Central Plains without shame.”

The heir of the Wang Family Estate, who had boasted endlessly about the greatness of his family’s martial arts, answered with a stern expression.

“I’m a saber user. I never learned sword arts.”

“What?”

“And why are you trying to dump this on me? If Young Lady Shin wants to stop him so badly, she can step in herself.”

“My goodness. What a ridiculous thing to say.”

That was when the young prodigies of the Five Gates began shoving the responsibility onto one another.

Hyuk Mujin, who had been quietly watching the situation, suddenly cut in.

“You’re all worrying over nothing. If it were me, I’d hurry over and lend a hand, at least.”

“You—no, you. Who are you?”

With such a terrifying scene unfolding before them, they had to speak with even an ordinary martial artist using half-polite language.

Young Lady Hwang, who had received Shu brocade as a gift from Woo Jintae only moments earlier, quickly stepped forward.

“Let me make this clear in advance. We have no ill feelings toward you people. You know that, right?”

“Do you? If that’s how it is, then fine. Let’s say that’s how it is.”

“I’m not saying we should just say that. I’m saying it’s the truth.”

“What good does telling me do?”

Hyuk Mujin smiled thinly and jerked his chin toward Jin Taekyung’s back, where he was enthusiastically beating Woo Jintae.

“Our Captain has quite a temper. Once the gentleman getting beaten over there collapses, who do you think will be next? You, Young Master? Or the Young Lady beside you?”

“…”

“Oh, and just in case you’re wondering, that man hits men and women alike.”

“I-I didn’t laugh!”

“Neither did I!”

“Do I have to say the same thing twice? Telling me won’t do you any good. Though, there is one way that might work.”

“A way?”

The young prodigies’ ears perked up.

They hadn’t trained in martial arts for nothing. They understood that they had no chance against that monstrous young man.

“P-please… somebody save me…”

Woo Jintae’s dying voice happened to drift into their ears, fanning their survival instincts even further.

“W-what exactly is this way?”

Hyuk Mujin stroked his chin with a deliberately serious expression.

“Well, you’re all children of families that can fart with the best of them, so I don’t know whether you’ll be able to do it.”

“I will!”

“I’ll do it! I’ll definitely do it!”

“Good. You know the basics.”

Hyuk Mujin nodded with satisfaction and pointed to Cheongpung, who was watching the one-sided beating with his mouth hanging open.

“First, apologize politely to this gentleman.”

Before he had even finished speaking, the young men and women of the Five Gates bent at the waist.

“We sincerely apologize.”

“We’re truly sorry for judging you rashly based on your appearance.”

Cheongpung scratched the back of his head.

“I’m fine, so everyone can stand up.”

Hyuk Mujin was taken aback by how readily Cheongpung forgave them, especially after they had mocked him in front of so many people.

Even the expression on his face, which should have been flushed with anger, was sunny and bright.

“You’re saying that so easily?”

“Yes. Is there a problem?”

“It’s not that, but… Weren’t you angry earlier? You were insulted so publicly.”

“Why would I be angry? I just thought it was fascinating.”

“What?”

“It was the first time so many people had focused on me like that. It was also the first time someone who had looked down on me apologized. I thought it was fascinating and fun.”

“…”

“Ah. I think coming down from the mountain was a good decision.”

*This guy’s a little nuts, too.*

Hyuk Mujin looked at Cheongpung as though he were some strange creature, then shook his head and turned to the young prodigies.

“You heard him, right? Since the Young Hero here has accepted your apology, we’ll consider the matter settled.”

“Oh!”

“We’re saved!”

But Hyuk Mujin wasn’t finished.

“All right, then. There’s one final thing left—the second.”

“…The second?”

“There’s more?”

“Yes. This is the most important one.”

Then, with a solemn expression, he declared to the four men and women looking at him,

“All of you, bend over and plant your heads on the floor.”

“……!”

“……”
```
